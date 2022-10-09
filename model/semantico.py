from email import parser
import ply.yacc as yacc
from model.lexicoAux import tokens

resultado_lexema = []
nombre = []
valoresVariable = []

precedence = (
    ("izquierda", "LPAREN", "RPAREN", "LLLAVE", "RLLAVE", "PUNTO"),
    ("izquierda", "MENORQUE", "MAYORQUE"),
    ("izquierda", "IGUALIGUAL", "DISTINTO"),
    ("izquierda", "COMA"),
)


def p_inicio(p):
    """inicio : MET ID LPAREN RPAREN LLLAVE instrucciones RLLAVE"""
    pass


def p_instrucciones(p):
    """
    instrucciones : variable instrucciones
    instrucciones : si instrucciones
    instrucciones : imprimir instrucciones
    instrucciones : empty
    """
    pass


def p_variable(p):
    """variable : ID IGUAL tipodato LPAREN datos RPAREN PUNTOCOMA"""
    nombre.append(str(p[1]))
    valoresVariable.append(str(p[5]))
    print(valoresVariable)
    p[0] = p[1]


def p_tipodato(p):
    """
    tipodato : INT
    tipodato : FLOAT
    tipodato : STRING
    """
    pass


def p_datos(p):
    """
    datos : NUMERO
    datos : NUMERO PUNTO NUMERO
    datos : CADENA
    datos : empty
    """
    try:
        p[0] = str(p[1]) + str(p[2]) + str(p[3])
    except LookupError:
        p[0] = p[1]


def p_if(p):
    """
    si : IF LPAREN evaluar RPAREN LLLAVE instrucciones RLLAVE
    """
    print(str(p[3]))
    if p[3]:
        p[0] = p[6]
        print("if si cumple")
    else:
        print("NO CUMPE")

def p_imprimir(p):
    """
    imprimir : WRITE DOSPUNTOS mensaje 
    """


def p_mensaje(p):
    '''
    mensaje : datosM PUNTOCOMA 
    mensaje : ID PUNTOCOMA 
    mensaje : datosM COMA mensaje
    mensaje : ID COMA mensaje
    mensaje : datosM COMA ID mensaje
    '''
    # if str(p[1]) in nombre:
    #     print("valor en id 1,",str(p[1]))
    # elif str(p[3]) in nombre:
    #     print("valor del id, ",str(p[3]))
    # else:
    print("Solo es impresion",str(p[1]))
    
def p_datosM(p):
    '''
    datosM : NUMERO
    datosM : NUMERO PUNTO NUMERO
    datosM : CADENA
    '''
    p[0] = p[1] 
    
def p_evaluar(p):
    """
    evaluar : ID comparar ID
    evaluar : NUMERO comparar NUMERO
    evaluar : ID comparar NUMERO
    evaluar : NUMERO comparar ID
    """
    guardarDig = "".join(str(p[1]))
    guardarDig2 = "".join(str(p[3]))
    if guardarDig.isdigit() and guardarDig2.isdigit():
        if str(p[2]) == "<":
            p[0] = str(p[1]) < str(p[3])
        if str(p[2]) == ">":
            p[0] = str(p[1]) > str(p[3])
        if str(p[2]) == "<=":
            p[0] = str(p[1]) <= str(p[3])
        if str(p[2]) == ">=":
            p[0] = str(p[1]) >= str(p[3])
        if str(p[2]) == "==":
            p[0] = str(p[1]) == str(p[3])
    elif guardarDig.isdigit():
        valor2 = valoresVariable[nombre.index(str(p[3]))]
        if valor2 == "None" and guardarDig2.isdigit():
            p[0] = False
        else:
            if str(p[2]) == "<":
                p[0] = str(p[1]) < str(p[3])
            if str(p[2]) == ">":
                p[0] = str(p[1]) > str(p[3])
            if str(p[2]) == "<=":
                p[0] = str(p[1]) <= str(p[3])
            if str(p[2]) == ">=":
                p[0] = str(p[1]) >= str(p[3])
            if str(p[2]) == "==":
                p[0] = str(p[1]) == str(p[3])
    elif guardarDig2.isdigit():
        valor1 = valoresVariable[nombre.index(str(p[1]))]
        if valor1 == "None" and guardarDig.isdigit():
            p[0] = False
        else:
            if str(p[2]) == "<":
                p[0] = str(p[1]) < str(p[3])
            if str(p[2]) == ">":
                p[0] = str(p[1]) > str(p[3])
            if str(p[2]) == "<=":
                p[0] = str(p[1]) <= str(p[3])
            if str(p[2]) == ">=":
                p[0] = str(p[1]) >= str(p[3])
            if str(p[2]) == "==":
                p[0] = str(p[1]) == str(p[3])
    elif (
        valoresVariable[nombre.index(str(p[1]))] != "None"
        and valoresVariable[nombre.index(str(p[3]))] != "None"
    ):
        if str(p[2]) == "<":
            if valoresVariable[nombre.index(str(p[1]))] < valoresVariable[nombre.index(str(p[3]))]:
                p[0] = True
            else:
                p[0] = False
        if str(p[2]) == ">":
            if valoresVariable[nombre.index(str(p[1]))] > valoresVariable[nombre.index(str(p[3]))]:
                p[0] = True
            else:
                p[0] = False
        if str(p[2]) == "<=":
            if valoresVariable[nombre.index(str(p[1]))] <= valoresVariable[nombre.index(str(p[3]))]:
                p[0] = True
            else:
                p[0] = False
        if str(p[2]) == ">=":
            if valoresVariable[nombre.index(str(p[1]))] >= valoresVariable[nombre.index(str(p[3]))]:
                p[0] = True
            else:
                p[0] = False
        if str(p[2]) == "==":
            if valoresVariable[nombre.index(str(p[1]))] == valoresVariable[nombre.index(str(p[3]))]:
                p[0] = True
            else:
                p[0] = False





def p_comprar(p):
    """
    comparar : IGUALIGUAL
    comparar : MENORQUE
    comparar : MAYORQUE
    comparar : MENORIGUAL
    comparar : MAYORIGUAL
    """
    p[0] = p[1]


def p_empty(p):
    """empty :"""
    pass


def p_error(p):
    global resultado_lexema
    resultado_lexema.clear()
    resultado_lexema.append(str(p))
    print("SI ENTRO A ERROR Y ES ESTE -> ", str(p))


parser = yacc.yacc()


def semantico(data):
    global resultado_lexema
    resultado_lexema.clear()
    result = parser.parse(data)
    # resultado_lexema.append(str(result))
    return resultado_lexema

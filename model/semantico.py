from email import parser
import ply.yacc as yacc
from model.lexicoAux import tokens

resultado_lexema = []
nombre = []
valoresVariable = []
mensajeBien = []
guardarMensaje = []
cantidadVuelta = []

precedence = (
    ("lef", "LPAREN", "RPAREN", "LLLAVE", "RLLAVE", "PUNTO"),
    ("left", "MENORQUE", "MAYORQUE"),
    ("left", "IGUALIGUAL", "DISTINTO"),
    ("left", "COMA"),

)

# precedence = (
#     ('left', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'POINT'),
#     ('left', 'TIMES', 'DIVIDE'),
#     ('left', 'PLUS', 'MINUS'),
#     ('left', 'LESS', 'LESSEQUAL', 'GREATER', 'GREATEREQUAL'),
#     ('left', 'DEQUAL', 'DISTINT'),
#     ('left', 'COMMA'),
#     ('right', 'PLUSPLUS', 'MINUSMINUS'),
# )



def p_inicio(p):
    """inicio : MET ID LPAREN RPAREN LLLAVE instrucciones RLLAVE"""
    p[0] = p[6]


def p_instrucciones(p):
    """
    instrucciones : variable instrucciones
    instrucciones : si instrucciones
    instrucciones : imprimir instrucciones
    instrucciones : for instrucciones
    instrucciones : empty
    """
    p[0] = p[1]

def p_for(p):
    """
    for : FOR LPAREN ID TO valor RPAREN LLLAVE instrucciones RLLAVE
    """
    i = int(str(p[5]))
    x = 0
    while x < i:
        p[0] = p[8]
        print(p[8])
        x = x + 1
    p[0] = p[8]



def p_valor(p):
    """
    valor : NUMERO
    valor : ID
    """
    if str(p[1]) in nombre:
        p[0] = valoresVariable[nombre.index(str(p[1]))]
    else:
        p[0] = p[1]

def p_variable(p):
    """variable : ID IGUAL tipodato LPAREN datos RPAREN PUNTOCOMA"""
    nombre.append(str(p[1]))
    valoresVariable.append(str(p[5]))
    
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
    datos : MINUS NUMERO
    datos : MINUS NUMERO PUNTO NUMERO
    datos : empty
    """
    try:
        if str(p[1]) == "-":
            p[0] = str(p[1]) + str(p[2]) + str(p[3]) + str(p[4])
        else:
            p[0] = str(p[1]) + str(p[2]) + str(p[3])
    except LookupError:
        if str(p[1]) == "-":
            print("SI", str(p[1]))
            p[0] = str(p[1]) + str(p[2])
        else:
            p[0] = p[1]


def p_if(p):
    """
    si : IF LPAREN evaluar RPAREN LLLAVE instrucciones RLLAVE else
    """
    if p[3]:
        p[0] = p[6]
        print("if si cumple ")
    else:
        p[0] = p[8]
        print("NO CUMPE")

def p_else(p):
    """
    else : ELSE LLLAVE instrucciones RLLAVE
    """
    p[0] = p[3]

def p_imprimir(p):
    """
    imprimir : WRITE DOSPUNTOS mensaje PUNTOCOMA
    """
    p[0] = p[3]


def p_mensaje(p):
    '''
    mensaje : datosM
    mensaje : ID 
    mensaje : datosM COMA mensajerep
    mensaje : ID COMA mensajerep
    mensaje : datosM COMA ID mensajerep
    '''
    if str(p[1]) != "None":
        if str(p[1]) in nombre and str(p[3]) == "None":
            p[0] = valoresVariable[nombre.index(str(p[1]))]
        elif str(p[1]) in nombre and str(p[3]) != "None":
            print("ENTRO")
            p[0] = valoresVariable[nombre.index(str(p[1]))] + str(p[3]) 
        elif str(p[1]) != "None" and str(p[3]) in nombre:
            p[0] = str(p[1]) + valoresVariable[nombre.index(str(p[3]))]
        else:
            p[0] = p[1]
    elif str(p[3]) in nombre and str(p[1]) != "None":
        p[0] = str(p[1]) + valoresVariable[nombre.index(str(p[3]))]
    elif str(p[3]) in nombre:
        print("ENTRO ACA PRIMERO WTF")
        p[0] = valoresVariable[nombre.index(str(p[3]))]
    elif str(p[1]) != "None" and str(p[3]) != "None":
        p[0] = str(p[1]) + str(p[3])
    

def p_mensajerep(p):
    """
    mensajerep : datosM
    mensajerep : ID
    """
    p[0] = p[1]

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
    global resultado_lexema,mensajeBien
    resultado_lexema.clear()
    result = parser.parse(data)
    for item in reversed(mensajeBien):
        guardarMensaje.append(item)
    mensajeBien.clear()
    print(guardarMensaje, " xd")
    # resultado_lexema.append(str(result))
    return resultado_lexema

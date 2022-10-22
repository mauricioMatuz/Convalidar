import ply.lex as lex

resultado_lexema = []

tokens = (
    "IF",
    "ELSE",
    "FOR",
    "STRING",
    "INT",
    "FLOAT",
    "WRITE",
    "IGUAL",
    "COMA",
    "LLLAVE",
    "RLLAVE",
    "LPAREN",
    "RPAREN",
    "ID",
    "DISTINTO",
    "NUMERO",
    "PUNTOCOMA",
    "MENORQUE",
    "MAYORQUE",
    "COMILLA",
    "PUNTO",
    "CADENA",
    "MET",
    "IGUALIGUAL",
    "MENORIGUAL",
    "MAYORIGUAL",
    "DOSPUNTOS",
    "TO",
    "MINUS",
    "PLUS"
)
t_MINUS = r"-"
t_PLUS = r"\+"
t_IGUAL = r"="
t_MENORQUE = r"<"
t_MAYORQUE = r">"
t_PUNTOCOMA = r";"
t_COMA = r","
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LLLAVE = r"{"
t_RLLAVE = r"}"
t_COMILLA = r"\""
t_PUNTO = r"\."
t_DOSPUNTOS = r":"


def t_WRITE(t):
    r"write"
    return t


def t_ELSE(t):
    r"else"
    return t

def t_TO(t):
    r"to"
    return t

def t_IF(t):
    r"if"
    return t


def t_INT(t):
    r"int"
    return t


def t_STRING(t):
    r"String"
    return t


def t_MET(t):
    r"Met"
    return t


def t_FLOAT(t):
    r"float"
    return t


def t_FOR(t):
    r"for"
    return t


def t_NUMERO(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_ID(t):
    r"\w+(_\d\w)*"
    return t


def t_MENORIGUAL(t):
    r"<="
    return t


def t_MAYORIGUAL(t):
    r">="
    return t


def t_IGUALIGUAL(t):
    r"=="
    return t


def t_DISTINTO(t):
    r"!="
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_CADENA(t):
    # expresion RE para reconocer los String
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t 
    # r" ?(\w+ \ *\w*\d* \ *) (\w+ \ *\w*\d* \ *) (\w+ \ *\w*\d* \ *) (\w+ \ *\w*\d* \ *)?"
    # return t


t_ignore = " \t\n\r"


def t_comments(t):
    r"/\*(.|\n)*?\*/"
    t.lexer.lineno += t.value.count("\n")


def t_comments_C99(t):
    r"//(.)*?\n"
    t.lexer.lineno += 1


def t_error(t):
    resultado_lexema.append("ERROR LEXICO " + str(t.value[0]))
    print(("Error Lexico: " + str(t.value[0])))
    t.lexer.skip(1)


def lexicoAux(data):
    global resultado_lexema
    analizador = lex.lex()
    analizador.input(data)
    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        # print("lexema de "+tok.type+" valor "+tok.value+" linea "tok.lineno)

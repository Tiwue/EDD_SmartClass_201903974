
from Estructuras.Nodos import NodoAnalisis
from analizador.analizador import tokens
from Estructuras.ListaAnalisis import ListaAnalisis



usuarios_Lista = ListaAnalisis()
tareas_Lista = ListaAnalisis()

nodo_elemento = NodoAnalisis()

names={}
def p_statement_group(t):
    'statement : LQUESTION TELEMENTS RQUESTION elementos LQUESTION DOLAR TELEMENTS RQUESTION'
    print('Ok')

def p_elementos_group(t):
    """elementos : elementos elemento
                 | elemento
    """

def p_elemento(t):
    'elemento : LQUESTION TELEMENT  tipoElemento RQUESTION items LQUESTION DOLAR TELEMENT RQUESTION'

    if t[3] == "user":
        usuarios_Lista.insertValue(nodo_elemento.carnet, nodo_elemento.dpi, nodo_elemento.nombre, nodo_elemento.carrera, nodo_elemento.password,
                              nodo_elemento.creditos, nodo_elemento.edad, nodo_elemento.correo, nodo_elemento.descripcion, nodo_elemento.materia,
                              nodo_elemento.fecha, nodo_elemento.hora, nodo_elemento.estado)
    else:
        tareas_Lista.insertValue(nodo_elemento.carnet, nodo_elemento.dpi, nodo_elemento.nombre, nodo_elemento.carrera, nodo_elemento.password,
                              nodo_elemento.creditos, nodo_elemento.edad, nodo_elemento.correo, nodo_elemento.descripcion, nodo_elemento.materia,
                              nodo_elemento.fecha, nodo_elemento.hora, nodo_elemento.estado)
    nodo_elemento.clean_values()

def p_tipoElemento(t):
    """tipoElemento : TTYPE EQUALS NORMSTRING
    """
    t[0] = t[3].replace('"', '').replace(' ', '')


def p_items(t):
    """items : items item
    """
    t[0] = t[2]

def p_items_2(t):
    """items : item
    """
    t[0] = t[1]

def p_item(t):
    """item : LQUESTION TITEM tipeItem EQUALS valueItem DOLAR RQUESTION
    """
    if t[3].lower() == "carnet":
        nodo_elemento.carnet = t[5].replace('"', '').strip()
    elif t[3].lower() == "dpi":
        nodo_elemento.DPI = t[5].replace('"', '').strip()
    elif t[3].lower() == "nombre":
        nodo_elemento.nombre = t[5].replace('"', '').strip()
    elif t[3].lower() == "carrera":
        nodo_elemento.carrera = t[5].replace('"', '').strip()
    elif t[3].lower() == "password":
        nodo_elemento.password = t[5].replace('"', '').strip()
    elif t[3].lower() == "creditos":
        nodo_elemento.creditos = t[5]
    elif t[3].lower() == "edad":
        nodo_elemento.edad = t[5]
    elif t[3].lower() == "correo":
        nodo_elemento.correo = t[5].replace('"', '').strip()
    elif t[3].lower() == "descripcion":
        nodo_elemento.descripcion = t[5].replace('"', '').strip()
    elif t[3].lower() == "materia":
        nodo_elemento.materia = t[5].replace('"', '').strip()
    elif t[3].lower() == "fecha":
        nodo_elemento.fecha = t[5].replace('"', '').strip()
    elif t[3].lower() == "hora":
        nodo_elemento.hora = t[5].replace('"', '').strip()
    elif t[3].lower() == "estado":
        nodo_elemento.estado = t[5].replace('"', '').strip()

    t[0] = nodo_elemento

def p_valueItem(t):
    """valueItem : NORMSTRING
                 | NUMBER
                 """
    t[0] = t[1]

def p_tipeItem(t):
    """tipeItem : TCARNET
                | TDPI
                | TNOMBRE
                | TCARRERA
                | TPASSWORD
                | TCREDITOS
                | TEDAD
                | TDESCRIPCION
                | TMATERIA
                | TFECHA
                | THORA
                | TESTADO
                | TCORREO
                """
    t[0] = t[1]

def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()
from Estructuras.MatrizTareas import MatrizTareas

class NodoMes:
    def __init__(self, mes):
        self.mes = mes
        self.tareas = MatrizTareas()
        self.next=None
        self.previous = None
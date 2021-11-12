from Estructuras.ListaSemestres import ListaSemestres
from Estructuras.ListaMeses import ListaMeses

class NodoAño:
    def __init__(self, año):
        self.año = año
        self.semestres = ListaSemestres()
        self.meses = ListaMeses()
        self.next=None
        self.previous = None  
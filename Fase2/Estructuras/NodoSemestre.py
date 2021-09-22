

class NodoSemestre:
    def __init__(self, semestre):
        self.semestre = semestre()
        self.cursos = None
        self.next=None
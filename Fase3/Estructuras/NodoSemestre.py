from Estructuras.ArbolCursos import ArbolCursos

class NodoSemestre:
    def __init__(self, semestre):
        self.semestre = semestre
        self.cursos = ArbolCursos()
        self.next=None
from Estructuras.NodoSemestre import NodoSemestre

class ListaSemestres:
    def __init__(self):
        self.Primero = None

    def getSize(self):
        aux = self.Primero
        contador = 0
        while aux is not None:
            contador += 1
            aux = aux.next
        return contador

    def isEmpty(self):
        return self.Primero is None

    def getList(self):
        aux = self.Primero
        while aux is not None:
            print(aux.año)
            aux = aux.next

    def add(self, semestre,curso):
        if self.exist(semestre):
            aux = self.Primero
            while aux is not None:
                if aux.semestre == semestre:
                    aux.cursos.InsertarDatos(int(curso.codigo), curso)
                aux = aux.next
        else:    
            nuevo = NodoSemestre(semestre)
            nuevo.cursos.InsertarDatos(int(curso.codigo), curso)
            if self.isEmpty():
                self.Primero = nuevo
            else:
                temp=self.Primero
                while temp.next is not None:
                    temp = temp.next
                temp.next=nuevo

    def exist(self,semestre):
        aux = self.Primero
        while aux is not None:
            if aux.semestre == semestre:
                return True
            aux = aux.next
        return False

    def graficarCursos(self, semestre, tipo):
        if self.exist(semestre):
            aux = self.Primero
            while aux is not None:
                if aux.semestre == semestre:
                    return aux.cursos.Graficar(tipo)
                aux = aux.next
        else:    
            return "no existe el semestre solicitado para graficar los cursos"                
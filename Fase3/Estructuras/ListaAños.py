from Estructuras.NodoAño import NodoAño

class ListaAños:
    def __init__(self):
        self.Primero = None
        self.Ultimo = None

    def getSize(self):
        aux = self.Primero
        contador = 0
        while aux is not None:
            contador += 1
            aux = aux.Next()

        return contador

    def isEmpty(self):
        return self.Primero is None

    def getList(self):
        aux = self.Primero
        while aux is not None:
            print(aux.año)
            aux = aux.Next

    def addTarea(self, año,mes, hora, dia, tarea):
        if self.exist(año):
            aux = self.Primero
            while aux is not None:
                if aux.año == año:
                    aux.meses.add(mes, hora, dia,tarea)
                aux = aux.next
        else:    
            nuevo = NodoAño(año)
            nuevo.meses.add(mes, hora, dia,tarea)
            if self.isEmpty():
                self.Ultimo = nuevo
                self.Primero = self.Ultimo
            else:
                self.Ultimo.Next = nuevo
                nuevo.Previous = self.Ultimo
                self.Ultimo = nuevo

    def addCurso(self, año, semestre, curso):
        if self.exist(año):
            aux = self.Primero
            while aux is not None:
                if aux.año == año:
                    aux.semestres.add(semestre, curso)
                aux = aux.next
        else:    
            nuevo = NodoAño(año)
            nuevo.semestres.add(semestre, curso)
            if self.isEmpty():
                self.Ultimo = nuevo
                self.Primero = self.Ultimo
            else:
                self.Ultimo.next = nuevo
                nuevo.Previous = self.Ultimo
                self.Ultimo = nuevo

    def exist(self,año):
        aux = self.Primero
        while aux is not None:
            if aux.año == año:
                return True
            aux = aux.next
        return False

    def graficarMatriz(self, año, mes):
        if self.exist(año):
            aux = self.Primero
            while aux is not None:
                if aux.año == año:
                    return aux.meses.graficarMatriz(mes)
                aux = aux.next
        else:    
            return "no existe el año solicitado para graficar la matriz"  

    def graficarLista(self, año, mes, dia, hora):
        if self.exist(año):
            aux = self.Primero
            while aux is not None:
                if aux.año == año:
                    return aux.meses.graficarLista(mes,dia,hora)
                aux = aux.next
        else:    
            return "no existe el año solicitado para graficar la matriz"

    def graficarCursos(self, año, semestre,tipo):
        if self.exist(año):
            aux = self.Primero
            while aux is not None:
                if aux.año == año:
                    return aux.semestres.graficarCursos(semestre,tipo)
                aux = aux.next
        else:    
            return "no existe el año solicitado para graficar los cursos"          
                               
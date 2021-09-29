

class NodoTarea:
    def __init__(self, tarea):
        self.tarea=tarea
        self.siguiente=None

class ListaTareas:
    def __init__(self):
        self.Primero=None

    def isEmpty(self):
        if self.Primero==None:
            return True
        else:
            return False

    def getList(self):
        aux = self.Primero
        while aux is not None:
            print(aux.tarea.toString())
            aux = aux.siguiente

    def add(self, tarea):
        if not self.exist(tarea):
            nuevo = NodoTarea(tarea)
            if self.isEmpty():
                self.Primero=nuevo
            else:
                aux=self.Primero
                while aux.siguiente is not None:
                    aux = aux.siguiente
                aux.siguiente=nuevo

    def length(self):
        counter=0
        if self.isEmpty():
            return counter
        else:
            aux=self.Primero
            while aux != None:
                counter += 1
                aux = aux.siguiente
            return counter

    def exist(self, tarea):
        aux = self.Primero
        while aux is not None:
            if aux.tarea.descripcion == tarea.descripcion and aux.tarea.materia == tarea.materia:
                return True
            aux = aux.siguiente
        return False                

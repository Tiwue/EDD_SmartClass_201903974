

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
        nuevo = NodoTarea(tarea)
        if self.isEmpty():
            self.Primero=nuevo
        else:
            aux=self.Primero
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente=nuevo

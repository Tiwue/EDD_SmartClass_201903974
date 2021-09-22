from Estructuras.NodoMes import NodoMes




class ListaMeses:
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

    def insertValue(self, mes):
        nuevo = NodoMes(mes)
        if self.isEmpty():
            self.Ultimo = nuevo
            self.Primero = self.Ultimo
        else:
            self.Ultimo.Next = nuevo
            nuevo.Previous = self.Ultimo
            self.Ultimo = nuevo
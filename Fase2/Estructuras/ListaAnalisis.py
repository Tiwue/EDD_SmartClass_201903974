from Estructuras.Nodos import NodoAnalisisS


class ListaAnalisis:
    def __init__(self):
        self.Primero = None
        self.Ultimo = None

    def getSize(self):
        aux = self.Primero
        contador = 0
        while aux is not None:
            contador += 1
            aux = aux.next()

        return contador

    def isEmpty(self):
        return self.Primero is None

    def getList(self):
        aux = self.Primero
        while aux is not None:
            print(aux.carnet + " - " + aux.nombre + "-" + aux.dpi + "-" + aux.descripcion + "-" + aux.fecha + "-" + aux.hora)
            aux = aux.next

    def insertValue(self, carnet, dpi, nombre, carrera, password, creditos, edad, correo, descripcion, materia, fecha, hora, estado):
        nuevo = NodoAnalisisS(carnet, dpi, nombre, carrera, password, creditos, edad, correo, descripcion, materia, fecha, hora, estado)

        if self.isEmpty():
            self.Ultimo = nuevo
            self.Primero = self.Ultimo
        else:
            self.Ultimo.next = nuevo
            nuevo.previous = self.Ultimo
            self.Ultimo = nuevo

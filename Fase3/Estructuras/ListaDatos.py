from Estructuras.NodoDoble import NodoDoble
class ListaDatos:
    def __init__(self):
        self.cuenta=0
        self.Primero=None
        self.Ultimo=None

    def isEmpty(self):
        return self.Primero==None

    def InsertarNodoD(self, codigo, curso):
        nuevo= NodoDoble(codigo,curso)
        if self.cuenta<4:
            if self.isEmpty():
                self.Primero=nuevo
                self.Ultimo=self.Primero
            else:
                self.Ultimo.siguiente=nuevo
                nuevo.Anterior=self.Ultimo
                self.Ultimo=nuevo
            self.cuenta +=1
        else:
            print("Ya se ha superado el tamaño")
    
    def InsertarDato(self, codigo, posicion):
        aux=self.Primero
        while posicion != 0:
            posicion-=1
            aux=aux.siguiente
        aux.codigo=codigo
    
    def DevolverDato(self, posicion):
        aux=self.Primero
        while posicion != 0:
            posicion-=1
            aux=aux.siguiente
        return aux

    def MostrarDatos(self):
        aux=self.Primero
        while aux is not None:
            print("Dato " + aux.codigo)
            aux=aux.siguiente
from Estructuras.NodoPuntero import NodoPuntero

class ListaPuntero:
    def __init__(self):
        self.Primero=None
        self.Ultimo=None
        self.cuenta=0

    def isEmpty(self):
        if self.Primero==None:
            return True
        else:
            return False

    def InsertarPuntero(self, puntero):
        nuevo = NodoPuntero(puntero)
        if self.cuenta<5:
            if self.isEmpty():
                self.Primero=nuevo
                self.Ultimo=self.Primero
            else:
                self.Ultimo.siguiente=nuevo
                nuevo.Anterior=self.Ultimo
                self.Ultimo=nuevo
            self.cuenta+=1

    def InsertarPunteroP(self, pagina,posicion):
        aux=self.Primero
        while posicion != 0:
            posicion-=1
            aux=aux.siguiente
        aux.puntero=pagina

    def DevolverPuntero(self,posicion):
        aux=self.Primero
        while posicion != 0:
            posicion-=1
            aux=aux.siguiente
        return aux

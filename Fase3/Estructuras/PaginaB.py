from Estructuras.ListaDatos import ListaDatos
from Estructuras.ListaPuntero import ListaPuntero
from Estructuras.ListaDatos import ListaDatos
class PaginaB:
    def __init__(self):
        self.punteros=ListaPuntero()
        self.datos=ListaDatos()
        self.maxClaves=5
        self.Cuenta=0

        for i in range(0, 5):
            if i != 4:
                self.datos.InsertarNodoD("", None)
            
            self.punteros.InsertarPuntero(None)

    def paginaLlena(self):
        return self.Cuenta==self.maxClaves-1
    
    def paginaCasiLLena(self):
        return self.Cuenta==self.maxClaves/2
    
    def getCodigo(self, posicion):
        return self.datos.DevolverDato(posicion).codigo
    
    def setCodigo(self, posicion,codigo):
        self.datos.InsertarDato(codigo, posicion)
    
    
    def getCurso(self,posicion):
        return self.datos.DevolverDato(posicion).curso

    
    def setCurso(self, posicion, curso):
        self.datos.DevolverDato(posicion).curso=curso
    
    def getApuntador(self, posicion):
        return self.punteros.DevolverPuntero(posicion).puntero
    
    def setApuntador(self, posicion,puntero):
        self.punteros.InsertarPunteroP(puntero, posicion)
    
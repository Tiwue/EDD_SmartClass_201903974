from Estructuras.Nodos import NodoAVL

class ArbolEstudiantes:

    def __init__(self):
        self.raiz=None

    def max(self, val1, val2):
        if val1 > val2:
            return val1
        else:
            return val2

    def altura(self, nodo):
        if nodo is not None:
            return nodo.altura
        return -1

    def insertar(self, estudiante):
        self.raiz = self.insert_inter(estudiante, self.raiz)  

    def insert_inter(self, estudiante, raiz):                
        if raiz is None:
            return NodoAVL(estudiante)
        else:
            if int(estudiante.carnet)< int(raiz.estudiante.carnet):
                raiz.izq = self.insert_inter(estudiante, raiz.izq)
                if self.altura(raiz.der)-self.altura(raiz.izq)==-2:
                    if int(estudiante.carnet)<int(raiz.izq.estudiante.carnet):
                        raiz = self.RI(raiz)
                    else:
                        raiz= self.RDI(raiz)
            elif int(estudiante.carnet)> int(raiz.estudiante.carnet):            
                raiz.der = self.insert_inter(estudiante,raiz.der)
                if self.altura(raiz.der)-self.altura(raiz.izq)==2:
                    if int(estudiante.carnet) > int(raiz.izq.estudiante.carnet):
                        raiz = self.RD(raiz)
                    else:
                        raiz = self.RDD(raiz)
            else:
                raiz.estudiante.carnet = estudiante.carnet            
        raiz.altura = self.max(self.altura(raiz.izq), self.altura(raiz.der))+1
        return raiz

    def RI(self, nodo):
        aux = nodo.izq
        nodo.izq= aux.der
        aux.der = nodo
        nodo.altura= self.max(self.altura(nodo.izq), self.altura(nodo.der))+1
        aux.altura = self.max(self.altura(aux.izq), self.altura(aux.der))+1
        return aux

    def RD(self, nodo):
        aux = nodo.der
        nodo.der= aux.izq
        aux.izq = nodo
        nodo.altura= self.max(self.altura(nodo.izq), self.altura(nodo.der))+1
        aux.altura = self.max(self.altura(aux.izq), self.altura(aux.der))+1
        return aux

    def RDI(self,nodo):
        nodo.izq = self.RD(nodo.izq)
        return self.RI(nodo)

    def RDD(self, nodo):
        nodo.der = self.RI(nodo.der)
        return self.RD(nodo)

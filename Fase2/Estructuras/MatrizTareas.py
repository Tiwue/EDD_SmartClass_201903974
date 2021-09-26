from Estructuras.Encabezado import listaEncabezado
from Estructuras.ListaTareas import ListaTareas
class NodoEncabezado:
	def __init__(self, index):
		self.index = index
		self.anterior = None
		self.siguiente = None
		self.accesoNodo=None

class Nodocelda:
	def __init__(self, fila, columna):
		self.tareas = ListaTareas()
		self.fila = fila
		self.columna = columna
		self.arriba = None
		self.abajo = None 
		self.derecha = None 
		self.izquierda = None    

class MatrizTareas:
    def __init__(self):
        self.efilas=listaEncabezado()
        self.ecolumnas=listaEncabezado()
      

    def add(self,fila, columna, tarea):
        nuevo = Nodocelda(fila, columna)
        nuevo.tareas.add(tarea)
        encabezadoFilas=self.efilas.getEncabezado(fila)
        if encabezadoFilas == None:
            encabezadoFilas= NodoEncabezado(fila)
            encabezadoFilas.accesoNodo=nuevo
            self.efilas.setEncabezado(encabezadoFilas)
        else:
            if self.existColumna(columna, encabezadoFilas.accesoNodo):
                aux=encabezadoFilas.accesoNodo
                while aux != None:
                    if aux.columna ==columna:
                        aux.tareas.add(tarea)
                        break
                    aux=aux.derecha

            else:    
                if int(nuevo.columna) < int(encabezadoFilas.accesoNodo.columna):
                    nuevo.derecha=encabezadoFilas.accesoNodo
                    encabezadoFilas.accesoNodo.izquierda=nuevo
                    encabezadoFilas.accesoNodo=nuevo
                else:
                    actual=encabezadoFilas.accesoNodo
                    while actual.derecha!=None:
                        if int(nuevo.columna) < int(actual.derecha.columna):
                            nuevo.derecha=actual.derecha
                            actual.derecha.izquierda =nuevo
                            nuevo.izquierda = actual
                            actual.derecha= nuevo
                            break
                        actual=actual.derecha

                    if actual.derecha == None:
                        actual.derecha=nuevo
                        nuevo.izquierda =actual           

        encabezadoColumnas = self.ecolumnas.getEncabezado(columna)
        if encabezadoColumnas==None:
            encabezadoColumnas=NodoEncabezado(columna)
            encabezadoColumnas.accesoNodo=nuevo
            self.ecolumnas.setEncabezado(encabezadoColumnas)
        else:
            if self.existFila(fila, encabezadoFilas.accesoNodo):
                aux=encabezadoFilas.accesoNodo
                while aux != None:
                    if aux.fila ==fila:
                        aux.tareas.add(tarea)
                        break
                    aux=aux.abajo

            else:   

                if int(nuevo.fila) < int(encabezadoColumnas.accesoNodo.fila):
                    nuevo.abajo=encabezadoColumnas.accesoNodo
                    encabezadoColumnas.accesoNodo.arriba=nuevo
                    encabezadoColumnas.accesoNodo=nuevo
                else:
                    actual = encabezadoColumnas.accesoNodo
                    while actual.abajo != None:
                        if int(nuevo.fila) < int(actual.abajo.fila):
                            nuevo.abajo = actual.abajo.fila
                            nuevo.abajo = actual.abajo
                            actual.abajo.arriba=nuevo
                            nuevo.arriba = actual
                            actual.abajo = nuevo
                            break
                        actual = actual.abajo

                    if actual.abajo == None:
                        actual.abajo=nuevo
                        nuevo.arriba= actual

    def existColumna(self,index, nodo):
        while nodo != None:
            if nodo.columna == index:
                return True
            nodo=nodo.derecha
        return False

    def existFila(self,index, nodo):
        while nodo != None:
            if nodo.fila == index:
                return True
            nodo=nodo.abajo
        return False    

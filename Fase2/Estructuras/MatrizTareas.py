from Estructuras.Encabezado import listaEncabezado

class NodoEncabezado:
	def __init__(self, index):
		self.index = index
		self.anterior = None
		self.siguiente = None
		self.accesoNodo=None

class Nodocelda:
	def __init__(self, fila, columna, caracter):
		self.caracter = caracter
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
      

    def add(self,fila, columna, caracter):
        nuevo = Nodocelda(fila, columna, caracter)

        encabezadoFilas=self.efilas.getEncabezado(fila)
        if encabezadoFilas == None:
            encabezadoFilas= NodoEncabezado(fila)
            encabezadoFilas.accesoNodo=nuevo
            self.efilas.setEncabezado(encabezadoFilas)
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
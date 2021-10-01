from Estructuras.Encabezado import listaEncabezado
from Estructuras.ListaTareas import ListaTareas
from graphviz import Source
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
            if self.existFila(fila, encabezadoColumnas.accesoNodo):
                aux=encabezadoColumnas.accesoNodo
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

    def graficar(self, mes):
            cadena='graph grid{ layout=dot label="Recordatorios" labelloc = "t" node [shape=filled style="filled"];\n edge[dir=both style="solid", weight=1000];\n Mt[ label = "Mes:'+str(mes)+'", fillcolor = firebrick1, group=0];\n'
            aux1=self.ecolumnas.primero
            while aux1 != None:
                cadena += "D"+str(aux1.index)+'[label="Dia '+ str(aux1.index)+'", group='+str(aux1.index)+'];\n'
                aux1=aux1.siguiente
            aux2=self.efilas.primero
            while aux2 != None:
                cadena += "H"+str(aux2.index)+'[label="Hora '+ str(aux2.index) + ':00", group=0];\n'
                aux3=aux2.accesoNodo
                while aux3 != None:
                    cadena += "H"+str(aux3.fila)+"D"+str(aux3.columna)+'[label="'+str(aux3.tareas.length())+'", group='+str(aux3.columna)+']\n'
                    aux3=aux3.derecha
                aux2=aux2.siguiente

            aux8=self.efilas.primero
            cadena += "Mt --H"+str(aux8.index)
            aux8=aux8.siguiente 
            while aux8 != None:
                cadena +=" -- H"+str(aux8.index)
                aux8= aux8.siguiente
            cadena+="\n"

            aux4=self.ecolumnas.primero
            while aux4 != None:
                cadena += "D"+str(aux4.index)
                aux5=aux4.accesoNodo
                while aux5 != None:
                    cadena += " -- H"+str(aux5.fila)+"D"+str(aux5.columna)
                    aux5=aux5.abajo
                cadena += "\n"    
                aux4=aux4.siguiente
            
            aux8=self.ecolumnas.primero
            cadena += "rank=same {Mt--D"+str(aux8.index)
            aux8=aux8.siguiente 
            while aux8 != None:
                cadena +=" -- D"+str(aux8.index)
                aux8= aux8.siguiente
            cadena+="}\n"

            aux6=self.efilas.primero
            while aux6 != None:
                cadena += "	rank=same { H"+str(aux6.index)
                aux7=aux6.accesoNodo
                while aux7 != None:
                    cadena += " -- H"+str(aux7.fila)+"D"+str(aux7.columna)
                    aux7=aux7.derecha
                cadena += "}\n"    
                aux6=aux6.siguiente
        

            cadena +="}"
            s = Source(cadena, filename="Matriz",directory='C:\\Users\\steve\\Desktop\\Reportes_F2',format='pdf') 
            s.view()
            return "Matriz graficada exitosamente"        

    def graficarLista(self, mes, columna, fila):
        if self.efilas.exist(fila):
            aux=self.efilas.primero
            while aux !=None:
                if aux.index == fila:
                   aux2=aux.accesoNodo
                   while aux2!=None:
                       if aux2.columna == columna:
                           return aux2.tareas.graficar()
                       aux2=aux2.derecha
                aux=aux.siguiente               
            return "No existen recordatorios para el dia y hora solicitado"
        else:
            return "No existen recordatorios para el mes solicitado"




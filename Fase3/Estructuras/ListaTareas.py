from graphviz import Source

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
        if not self.exist(tarea):
            nuevo = NodoTarea(tarea)
            if self.isEmpty():
                self.Primero=nuevo
            else:
                aux=self.Primero
                while aux.siguiente is not None:
                    aux = aux.siguiente
                aux.siguiente=nuevo

    def length(self):
        counter=0
        if self.isEmpty():
            return counter
        else:
            aux=self.Primero
            while aux != None:
                counter += 1
                aux = aux.siguiente
            return counter

    def exist(self, tarea):
        aux = self.Primero
        while aux is not None:
            if aux.tarea.descripcion == tarea.descripcion and aux.tarea.materia == tarea.materia:
                return True
            aux = aux.siguiente
        return False

    def graficar(self):
        
        cadena='digraph G { label="RECORDATORIOS" labelloc="t" gradientangle=0 rankdir="LR" node[shape=note ] edge[dir=both, arrowhead=vee, arrowtail=vee];\n'
        aux=self.Primero
        contador=0
        while aux != None:
            contador +=1
            cadena += "nodo"+str(contador)+'[label="Carnet: '+str(aux.tarea.carnet)+'\\n'+'Nombre: '+aux.tarea.nombre+"\\nDescripcion: "+aux.tarea.materia+'\\nFecha: '+aux.tarea.fecha+"\\nHora: "+aux.tarea.hora+"\\nEstado: "+aux.tarea.estado+'" color="darkgray" ];\n'
            if aux.siguiente !=None:
                cadena +="nodo"+str(contador)+"->"+"nodo"+str(contador+1)+"\n"
            aux=aux.siguiente
        cadena +="}\n"    
        s=Source(cadena, filename="Lista Tareas",directory='C:\\Users\\steve\\Desktop\\Reportes_F2',format='pdf')
        s.view()
        return "Lista graficada con exito"
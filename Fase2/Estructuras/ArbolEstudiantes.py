from Estructuras.Nodos import NodoAVL
from graphviz import Source
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
                if (self.altura(raiz.der)-self.altura(raiz.izq))==-2:
                    if int(estudiante.carnet)<int(raiz.izq.estudiante.carnet):
                        raiz = self.RI(raiz)
                    else:
                        raiz= self.RDI(raiz)
            elif int(estudiante.carnet)> int(raiz.estudiante.carnet):            
                raiz.der = self.insert_inter(estudiante,raiz.der)
                if self.altura(raiz.der)-self.altura(raiz.izq)==2:
                    if int(estudiante.carnet) > int(raiz.der.estudiante.carnet):
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

    def buscar(self, carnet):
        
        if self.raiz is not None:
            return self.buscar_inter(self.raiz, carnet)
        else:
            return None    

    def buscar_inter(self, actual, carnet):
        if actual is not None:
            if actual.estudiante.carnet==carnet:
                return actual
            elif int(carnet) < int(actual.estudiante.carnet):
                return self.buscar_inter(actual.izq, carnet)
            else:
                return self.buscar_inter(actual.der, carnet)
        else:
            return None            

    def cargarCurso(self, carnet, año, semestre, curso):
        if self.raiz is not None:
            self.cargarCursos_inter(self.raiz, carnet, año, semestre, curso)
        else:
            print("No hay estudiantes cargados al sistema")

    def cargarCursos_inter(self, actual, carnet, año, semestre,curso):
        if actual is not None:
            if actual.estudiante.carnet==carnet:
                actual.estudiante.años.addCurso( año, semestre, curso)
            elif int(carnet) < int(actual.estudiante.carnet):
                self.cargarCursos_inter(actual.izq, carnet,año, semestre, curso)
            else:
                self.cargarCursos_inter(actual.der, carnet, año, semestre, curso)
        else:
            print("No se encontro un estudiante con este carnet")

    def cargarTarea(self, carnet, año, mes, hora, dia, tarea):
        if self.raiz is not None:
            self.cargarTarea_inter(self.raiz, carnet, año, mes, hora, dia, tarea)
        else:
            print("No hay estudiantes cargados al sistema")

    def cargarTarea_inter(self, actual, carnet, año, mes, hora,dia, tarea):
        if actual is not None:
            if actual.estudiante.carnet==carnet:
                actual.estudiante.años.addTarea( año, mes, hora , dia , tarea)
            elif int(carnet) < int(actual.estudiante.carnet):
                self.cargarTarea_inter(actual.izq, carnet,año, mes, hora, dia, tarea)
            else:
                self.cargarTarea_inter(actual.der, carnet, año, mes, hora, dia, tarea)
        else:
            print("No se encontro un estudiante con este carnet")


    def graficar(self):
            cadena='digraph G {rankdir="TB"\n node [margin=0.3 fontcolor=black  width=0.5 fontname="Comic Sans MS" shape=box3d style=filled]\n'
            if self.raiz is not None:
                cadena= self.graficar_inter(self.raiz, cadena)
            else:
                cadena += '"Aun no se cargan Estudiantes"'
            cadena += "}"
            s = Source(cadena, filename="Estudiantes",directory='C:\\Users\\steve\\Desktop\\Reportes_F2',format='pdf') 
            s.view()


    def graficar_inter(self, actual, cadena):        
        if actual is not None:
            cadena += actual.estudiante.carnet+'[fillcolor=gray84 label="'+actual.estudiante.carnet+"\\n"  +actual.estudiante.nombre+"\\n"+actual.estudiante.carrera+'"]\n'
            if actual.izq != None:
                cadena += actual.estudiante.carnet+"->"+actual.izq.estudiante.carnet+"\n"
                cadena = self.graficar_inter(actual.izq, cadena)
            if actual.der != None:
                cadena += actual.estudiante.carnet + "->"+ actual.der.estudiante.carnet+"\n"
                cadena = self.graficar_inter(actual.der, cadena )
        return cadena

    def graficarMatriz(self,carnet, año, mes):
        if self.raiz is not None:
            return self.graficarMatriz_inter(self.raiz, carnet, año, mes)
        else:
            return "No hay estudiantes cargados al sistema"

    def graficarMatriz_inter(self, actual, carnet, año, mes):
        if actual is not None:
            if actual.estudiante.carnet==carnet:
                return actual.estudiante.años.graficarMatriz(año,mes)
            elif int(carnet) < int(actual.estudiante.carnet):
                return self.graficarMatriz_inter(actual.izq, carnet,año,mes)
            else:
                return self.graficarMatriz_inter(actual.der, carnet, año, mes)
        else:
            return "No existe un estudiante con ese carnet"

    def graficarLista(self,carnet, año, mes, dia, hora):
        if self.raiz is not None:
            return self.graficarLista_inter(self.raiz, carnet, año, mes, dia, hora)
        else:
            return "No hay estudiantes cargados al sistema"

    def graficarLista_inter(self, actual, carnet, año, mes, dia, hora):
        if actual is not None:
            if actual.estudiante.carnet==carnet:
                return actual.estudiante.años.graficarLista(año,mes,dia,hora)
            elif int(carnet) < int(actual.estudiante.carnet):
                return self.graficarLista_inter(actual.izq, carnet,año,mes,dia,hora)
            else:
                return self.graficarLista_inter(actual.der, carnet, año, mes,dia,hora)
        else:
            return "No existe un estudiante con ese carnet"                  


    def graficarCursos(self,carnet, año, semestre, tipo):
        if self.raiz is not None:
            return self.graficarCursos_inter(self.raiz, carnet, año, semestre, tipo)
        else:
            return "No hay estudiantes cargados al sistema"

    def graficarCursos_inter(self, actual, carnet, año, semestre, tipo):
        if actual is not None:
            if actual.estudiante.carnet==carnet:
                return actual.estudiante.años.graficarCursos(año,semestre, tipo)
            elif int(carnet) < int(actual.estudiante.carnet):
                return self.graficarCursos_inter(actual.izq, carnet,año,semestre, tipo)
            else:
                return self.graficarCursos_inter(actual.der, carnet, año, semestre, tipo)
        else:
            return "No existe un estudiante con ese carnet"

    def modificar(self, carnet, dpi, nombre,carrera,correo,password, creditos,edad):
        
        if self.raiz is not None:
            return self.modificar_inter(self.raiz, carnet, dpi, nombre,carrera,correo,password, creditos,edad)
        else:
            return "No existen estudiantes cargados al sistema"    

    def modificar_inter(self, actual, carnet, dpi, nombre,carrera,correo,password, creditos,edad):
        if actual is not None:
            if actual.estudiante.carnet==carnet:
                actual.estudiante.dpi=dpi
                actual.estudiante.nombre=nombre
                actual.estudiante.carrera=carrera
                actual.estudiante.correo=correo
                actual.estudiante.password=password
                actual.estudiante.creditos=creditos
                actual.estudiante.edad=edad
                return "Estudiante modificado con exito"
            elif int(carnet) < int(actual.estudiante.carnet):
                return self.modificar_inter(actual.izq, carnet, dpi, nombre,carrera,correo,password, creditos,edad)
            else:
                return self.modificar_inter(actual.der, carnet, dpi, nombre,carrera,correo,password, creditos,edad)
        else:
            return "No se encontró un estudiante con ese carnet"

    def eliminar(self, carnet):
        if self.raiz is not None:
            return self.eliminar_inter(self.raiz,carnet)
        else:
            return "No existen estudiantes cargados al sistema"

    def eliminar_inter(self,actual,carnet):
        if actual is not None:
            if actual.estudiante.carnet==carnet:
                aux=actual.der
                if actual.izq is not None:
                    nuevo= self.ultimoDer(actual)
                    self.setNone(nuevo.estudiante.carnet)
                    actual.estudiante=nuevo.estudiante
                    if nuevo.izq is not None:
                        self.insertarElim(nuevo.izq)
                    if nuevo.der is not None:
                        self.insertarElim(nuevo.der)
                    actual.der=None
                    self.insertarElim(aux)    
                    return "Estudiante Eliminado"
                else:
                    actual=actual.der
                    return "Estudiante Eliminado"
                

            elif int(carnet) < int(actual.estudiante.carnet):
                return self.eliminar_inter(actual.izq, carnet)
            else:
                return self.eliminar_inter(actual.der, carnet)
        else:
            return "No se encontró un estudiante con ese carnet"    
    
    def ultimoDer(self, actual):
        if actual is not None:
            if actual.izq is not None:
                actual=actual.izq
                while actual.der is not None:
                    actual=actual.der
        return actual

    def setNone(self, carnet):
        if self.raiz is not None:
            self.setNone_inter(self.raiz, carnet)

    def setNone_inter(self, actual, carnet):
        if actual is not None:
            if actual.estudiante.carnet==carnet:
                actual=None
            elif int(carnet) < int(actual.estudiante.carnet):
                self.setNone_inter(actual.izq, carnet)
            else:
                self.setNone_inter(actual.der, carnet)

    def insertarElim(self, actual):
        if actual is not None:
            self.insertar(actual.estudiante)
            if actual.izq is not None:
                self.insertarElim(actual.izq)
            if actual.der is not None:
                self.insertarElim(actual.der)    



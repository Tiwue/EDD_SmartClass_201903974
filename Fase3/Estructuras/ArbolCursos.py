from Estructuras.NodoArbolCursos import NodoAVL
from graphviz import Source
class ArbolCursos:

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

    def insertar(self, curso):
        self.raiz = self.insert_inter(curso, self.raiz)  

    def insert_inter(self, curso, raiz):                
        if raiz is None:
            return NodoAVL(curso)
        else:
            if int(curso.codigo)< int(raiz.curso.codigo):
                raiz.izq = self.insert_inter(curso, raiz.izq)
                if (self.altura(raiz.der)-self.altura(raiz.izq))==-2:
                    if int(curso.codigo)<int(raiz.izq.curso.codigo):
                        raiz = self.RI(raiz)
                    else:
                        raiz= self.RDI(raiz)
            elif int(curso.codigo)> int(raiz.curso.codigo):            
                raiz.der = self.insert_inter(curso,raiz.der)
                if self.altura(raiz.der)-self.altura(raiz.izq)==2:
                    if int(curso.codigo) > int(raiz.der.curso.codigo):
                        raiz = self.RD(raiz)
                    else:
                        raiz = self.RDD(raiz)
            else:
                raiz.curso.codigo = curso.codigo            
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

    def buscar(self, codigo):
        
        if self.raiz is not None:
            return self.buscar_inter(self.raiz, codigo)
        else:
            return None    

    def buscar_inter(self, actual, codigo):
        if actual is not None:
            if actual.curso.codigo==codigo:
                return actual
            elif int(codigo) < int(actual.curso.codigo):
                return self.buscar_inter(actual.izq, codigo)
            else:
                return self.buscar_inter(actual.der, codigo)
        else:
            return None            

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
            cadena += actual.curso.codigo+'[fillcolor=gray84 label="'+actual.curso.codigo+"\\n"  +actual.curso.nombre+"\\n"+actual.curso.carrera+'"]\n'
            if actual.izq != None:
                cadena += actual.curso.codigo+"->"+actual.izq.curso.codigo+"\n"
                cadena = self.graficar_inter(actual.izq, cadena)
            if actual.der != None:
                cadena += actual.curso.codigo + "->"+ actual.der.curso.codigo+"\n"
                cadena = self.graficar_inter(actual.der, cadena )
        return cadena


    def modificar(self, codigo, dpi, nombre,carrera,correo,password, creditos,edad):
        
        if self.raiz is not None:
            return self.modificar_inter(self.raiz, codigo, dpi, nombre,carrera,correo,password, creditos,edad)
        else:
            return "No existen cursos cargados al sistema"    

    def modificar_inter(self, actual, codigo, dpi, nombre,carrera,correo,password, creditos,edad):
        if actual is not None:
            if actual.curso.codigo==codigo:
                actual.curso.dpi=dpi
                actual.curso.nombre=nombre
                actual.curso.carrera=carrera
                actual.curso.correo=correo
                actual.curso.password=password
                actual.curso.creditos=creditos
                actual.curso.edad=edad
                return "Estudiante modificado con exito"
            elif int(codigo) < int(actual.curso.codigo):
                return self.modificar_inter(actual.izq, codigo, dpi, nombre,carrera,correo,password, creditos,edad)
            else:
                return self.modificar_inter(actual.der, codigo, dpi, nombre,carrera,correo,password, creditos,edad)
        else:
            return "No se encontró un curso con ese codigo"
   
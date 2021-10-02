from Estructuras.PaginaB import PaginaB
from graphviz import Source
class ArbolCursos:
    def __init__(self):
        self.Raiz=None
        self.Codigo=None
        self.Curso=None
        self.auxiliar1=False
        self.Auxliar2=None
        self.subeArriba=False
        self.estado=False
        self.comparador=False
        self.grafica=""
        self.grafica2=""
        self.curso=None
        self.nodos=0

    def isEmpty(self, raiz):
        return raiz==None or raiz.Cuenta==0
        
    def InsertarDatos(self, codigo,curso):
        self.InsertarDatos2(self.Raiz,codigo,curso)
 
    def InsertarDatos2(self, raiz, codigo, curso):
            self.Empujar(raiz,codigo,curso)
            if self.subeArriba:
                self.Raiz= PaginaB()
                self.Raiz.Cuenta=1
                self.Raiz.setCodigo(0, self.Codigo)
                self.Raiz.setCurso(0, self.Curso)
                self.Raiz.setApuntador(0, raiz)
                self.Raiz.setApuntador(1, self.Auxliar2)
        
    def Empujar(self, raiz,codigo, curso):
            posicion=0
            self.estado=False
            
            if self.isEmpty(raiz) and self.comparador==False:
                self.subeArriba=True
                self.Codigo=codigo
                self.Curso=curso
                self.Auxliar2=None
            else:
                posicion=self.BuscarNodoB(codigo,raiz)
                if self.comparador==False:
                    if self.estado:
                        self.subeArriba=False
                    else:
                        self.Empujar(raiz.getApuntador(posicion),codigo,curso)
                        if self.subeArriba:
                            if raiz.Cuenta<4:
                                self.subeArriba=False
                                self.MeterHoja(raiz,posicion,self.Codigo,self.Curso)
                            else:
                                self.subeArriba=True
                                self.DividirPaginaB(raiz,posicion,self.Codigo,self.Curso)
                else:
                    print("Dato repetido"+ codigo)
                    self.comparador=False


    def BuscarNodoB(self, codigo, raiz):
        auxContador=0
        if codigo<raiz.getCodigo(0):
            self.estado=False
            auxContador=0
        else:
            while auxContador!=raiz.Cuenta:
                if codigo==raiz.getCodigo(auxContador):
                    self.comparador=True
                auxContador +=1 
            auxContador=raiz.Cuenta
            while codigo<raiz.getCodigo(auxContador-1) and auxContador>1:
                auxContador -=1
                if codigo==raiz.getCodigo(auxContador-1):
                    self.estado=True
                else:
                    self.estado=False     
        return auxContador
    
    def MeterHoja(self, raiz, posicion, codigo, curso):
        auxC=raiz.Cuenta
        while auxC != posicion:
            if auxC!=0:
                raiz.setCodigo(auxC, raiz.getCodigo(auxC-1))
                raiz.setCurso(auxC, raiz.getCurso(auxC-1))
                raiz.setApuntador(auxC+1, raiz.getApuntador(auxC))
            auxC-=1
        raiz.setCodigo(posicion, codigo)
        raiz.setCurso(posicion, curso)
        raiz.setApuntador(posicion+1, self.Auxliar2)
        raiz.Cuenta=raiz.Cuenta+1
    
    def DividirPaginaB(self, raiz, posicion, codigo, curso):
        posicion2=0
        posicionMedia=0
        
        if posicion<=2:
            posicionMedia=2
        else:
            posicionMedia=3
        
        paginaDerecha=PaginaB()
        posicion2=posicionMedia+1
        
        while posicion2!=5:
            
            if (posicion2-posicionMedia)!=0:
                paginaDerecha.setCodigo((posicion2-posicionMedia)-1, raiz.getCodigo(posicion2-1))
                paginaDerecha.setCurso((posicion2-posicionMedia)-1, raiz.getCurso(posicion2-1))
                paginaDerecha.setApuntador(posicion2-posicionMedia, raiz.getApuntador(posicion2))
            posicion2+=1
        paginaDerecha.Cuenta=4-posicionMedia
        raiz.Cuenta=posicionMedia
        
        if posicion<=2:
            self.auxiliar1=True
            self.MeterHoja(raiz,posicion,codigo,curso)
        else:
            self.auxiliar1=True
            self.MeterHoja(paginaDerecha,(posicion-posicionMedia),codigo,curso)
        
        self.Codigo=raiz.getCodigo(raiz.Cuenta-1)
        self.Curso=raiz.getCurso(raiz.Cuenta-1)
        
        paginaDerecha.setApuntador(0, raiz.getApuntador(raiz.Cuenta))
        
        raiz.Cuenta=raiz.Cuenta-1
        self.Auxliar2=paginaDerecha
        
        if self.auxiliar1:
            raiz.setCodigo(3, "")
            raiz.setCurso(3, "")
            raiz.setApuntador(4, None)
            
            raiz.setCodigo(2, "")
            raiz.setCurso(2, "")
            raiz.setApuntador(3, None)
            
    def Preorden(self):
        self.Preorden2(self.Raiz)
    
    def Preorden2(self, pagina):
        if pagina!=None:
            for i in range(0, pagina.Cuenta):
                if pagina.getCodigo(i)!=None:
                    if pagina.getCodigo(i)!="":
                       print(pagina.getCodigo(i)+"_")
            
            print("")
            
            self.Preorden2(pagina.getApuntador(0))
            self.Preorden2(pagina.getApuntador(1))
            self.Preorden2(pagina.getApuntador(2))
            self.Preorden2(pagina.getApuntador(3))
            self.Preorden2(pagina.getApuntador(4))      

    def getCursoM1(self, codigo):
        
        cursoB=None
        self.getCursoM(self.Raiz,codigo)
        cursoB=self.curso
        self.curso=None
        return cursoB
    
    def getCursoM(self, pagina, codigo):
        
        if pagina!=None:
            for i in range(0, pagina.Cuenta):
                if pagina.getCodigo(i)!=None:
                    if pagina.getCodigo(i)!=None:
                        if pagina.getCodigo(i)==codigo:
                            self.curso= pagina.getCurso(i)
            self.getCursoM(pagina.getApuntador(0),codigo)
            self.getCursoM(pagina.getApuntador(1),codigo)
            self.getCursoM(pagina.getApuntador(2),codigo)
            self.getCursoM(pagina.getApuntador(3),codigo)
            self.getCursoM(pagina.getApuntador(4),codigo)
            
    def Graficar(self, tipo):
        
        self.grafica="digraph ArbolB{\n"
        self.grafica+="\nrankdir=TB;\n"
        self.grafica+="node[color=\"greenyellow\",style=\"rounded,filled\",fillcolor=lightcyan3, shape=record];\n"
        self.Graficar2(self.Raiz)
        self.Graficar3(self.Raiz)
        self.grafica+="\n}\n"
        s = Source(self.grafica, filename=("Cursos"+tipo),directory='C:\\Users\\steve\\Desktop\\Reportes_F2',format='pdf') 
        s.view()
        return "Arbol Pensum graficado exitosamente"
    
    def Graficar2(self, pagina):
        contador=0
        if pagina!=None:
            self.nodos=0
            for i in range(0,pagina.Cuenta):
                if pagina.getCodigo(i)!=None:
                    if pagina.getCodigo(i)!="":
                        self.nodos+=1
                        if i!=0:
                            self.grafica+="|"
                        if self.nodos==1:
                            self.grafica+="\nNodo"+str(pagina.getCodigo(i))+"[label=\"<f0> |"
                        if i==0:
                            self.grafica+="<f"+str(i+1)+">"+str(pagina.getCodigo(i))+"\\n"+pagina.getCurso(i).nombre + "|<f"+str(i+2)+"> "
                            contador=3
                        else:
                            self.grafica+="<f"+str(contador)+">"+str(pagina.getCodigo(i))+"\\n"+pagina.getCurso(i).nombre + "|<f"+str(contador+1)+"> "
                            contador+=2
                        
                        if i==pagina.Cuenta-1:
                            contador=0;
                            self.grafica+=" \",group=0];\n"

            self.Graficar2(pagina.getApuntador(0))
            self.Graficar2(pagina.getApuntador(1))
            self.Graficar2(pagina.getApuntador(2))
            self.Graficar2(pagina.getApuntador(3))
            self.Graficar2(pagina.getApuntador(4))
    
    def Graficar3(self, pagina):
        if pagina!=None: 
            if pagina.getCodigo(0)!=None:
                    if pagina.getCodigo(0)!="":
                        if pagina.getApuntador(0)!=None and pagina.getApuntador(0).getCodigo(0)!=None:
                                self.grafica+="\nNodo"+str(pagina.getCodigo(0))+":f0->"+"Nodo"+str(pagina.getApuntador(0).getCodigo(0))
                        if pagina.getApuntador(1)!=None and pagina.getApuntador(1).getCodigo(0)!=None:
                                self.grafica+="\nNodo"+str(pagina.getCodigo(0))+":f2->"+"Nodo"+str(pagina.getApuntador(1).getCodigo(0))
                        if pagina.getApuntador(2)!=None and pagina.getApuntador(2).getCodigo(0)!=None:
                                self.grafica+="\nNodo"+str(pagina.getCodigo(0))+":f4->"+"Nodo"+str(pagina.getApuntador(2).getCodigo(0))
                        if pagina.getApuntador(3)!=None and pagina.getApuntador(3).getCodigo(0)!=None:
                                self.grafica+="\nNodo"+str(pagina.getCodigo(0))+":f6->"+"Nodo"+str(pagina.getApuntador(3).getCodigo(0))
                        if pagina.getApuntador(4)!=None and pagina.getApuntador(4).getCodigo(0)!=None:
                                self.grafica+="\nNodo"+str(pagina.getCodigo(0))+":f8->"+"Nodo"+str(pagina.getApuntador(4).getCodigo(0))

            self.Graficar3(pagina.getApuntador(0))
            self.Graficar3(pagina.getApuntador(1))
            self.Graficar3(pagina.getApuntador(2))
            self.Graficar3(pagina.getApuntador(3))
            self.Graficar3(pagina.getApuntador(4))
   
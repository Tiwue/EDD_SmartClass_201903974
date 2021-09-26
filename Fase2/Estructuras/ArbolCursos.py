from Estructuras.PaginaB import PaginaB
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
                ++auxContador 
            auxContador=raiz.Cuenta
            while codigo<raiz.getCodigo(auxContador-1) and auxContador>1:
                --auxContador
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
            
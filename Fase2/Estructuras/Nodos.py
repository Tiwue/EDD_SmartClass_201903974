

class NodoAnalisis:
    def __init__(self):
        self.type = ""
        self.carnet = ""
        self.dpi = ""
        self.nombre = ""
        self.carrera = ""
        self.password = ""
        self.creditos = 0
        self.edad = 0
        self.correo = ""
        self.descripcion = ""
        self.materia = ""
        self.fecha = ""
        self.hora = ""
        self.estado = ""

    def clean_values(self):
        self.type = ""
        self.carnet = ""
        self.dpi = ""
        self.nombre = ""
        self.carrera = ""
        self.password = ""
        self.creditos = 0
        self.edad = 0
        self.correo = ""
        self.descripcion = ""
        self.materia = ""
        self.fecha = ""
        self.hora = ""
        self.estado = ""

class NodoAnalisisS:
    def __init__(self, carnet, dpi, nombre, carrera, password, creditos, edad, correo, descripcion, materia, fecha, hora, estado):
        self.carnet = carnet
        self.dpi = dpi
        self.nombre = nombre
        self.carrera = carrera
        self.password = password
        self.creditos = creditos
        self.edad = edad
        self.correo = correo
        self.descripcion = descripcion
        self.materia = materia
        self.fecha = fecha
        self.hora = hora
        self.Estado = estado
        self.next = None
        self.previous = None
        

class NodoAVL:
    def __init__(self, estudiante):
        self.estudiante=estudiante
        self.izq=None
        self.der=None
        self.altura=0
            
    

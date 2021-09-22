from Estructuras.ListaAños import ListaAños

class Estudiante:
    def __init__(self, carnet, dpi, nombre, carrera, password, creditos, edad, correo):
        self.carnet = carnet
        self.dpi = dpi
        self.nombre = nombre
        self.carrera = carrera
        self.password = password
        self.creditos = creditos
        self.edad = edad
        self.correo = correo
        self.años=ListaAños()

class Tarea:
    def __init__(self, nombre, carnet, descripcion, materia, fecha, hora, estado, mes, dia):
        self.nombre = nombre
        self.carnet = carnet
        self.descripcion = descripcion
        self.materia = materia
        self.fecha = fecha
        self.estado = estado
        self.mes = mes 
        self.dia = dia 
        self.hora = hora

    def toString(self):
        cadena="Nombre: "+ self.nombre+"\nCarnet: "+self.carnet+"\nDescripcion: "+self.descripcion+"\nMateria: "+self.materia+"\nFecha: "+ self.fecha +"\nHora: "+self.hora
        return cadena
           
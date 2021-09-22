from flask import Flask, request, jsonify
import os
from analizador.sintactico import parser
from analizador.sintactico import usuarios_Lista, tareas_Lista
app=Flask(__name__)
ruta=os.getcwd()
from Estructuras.ArbolEstudiantes import ArbolEstudiantes
from Estructuras.Estudiante import Estudiante
Estudiantes= ArbolEstudiantes()

@app.route("/",methods=["GET"])
def inicio():
    return jsonify({"mensaje":"Server levantado :)"})
    
@app.route("/carga", methods=["POST"])
def carga():
    datos=request.get_json()
    print(datos["tipo"])
    print(datos["path"])
    try:
        archivo = open(datos["path"],"r",encoding="utf-8")
        mensaje = archivo.read()
        parser.parse(mensaje)
        archivo.close()
        if datos["tipo"] =="estudiante":
            temp = usuarios_Lista.Primero
            while temp is not None:
                estudiante1 = Estudiante(temp.carnet, temp.dpi, temp.nombre, temp.carrera, temp.password, temp.creditos, temp.edad, temp.correo)
                Estudiantes.insertar(estudiante1)
                temp = temp.next 
    except:
        print("no se pudo leer el archivo")
    print("------------------------")
    
    return jsonify({"mensaje":"Archivo leido :)"})
    
if __name__ == "__main__":
    app.run(port=3000)    

#'C:\\Users\\steve\\Desktop\\EDD\\EDD_SmartClass_201903974\\EDD_SmartClass_201903974\Fase2\codigo.txt'ruta+"\\Fase2\\"+
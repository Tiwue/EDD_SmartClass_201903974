from Estructuras.ArbolCursos import ArbolCursos
from flask import Flask, json, request, jsonify
import os
from analizador.sintactico import parser
from analizador.sintactico import usuarios_Lista, tareas_Lista
from Estructuras.ArbolEstudiantes import ArbolEstudiantes
from Estructuras.Estudiante import Estudiante
from Estructuras.Curso import Curso
from Estructuras.Tarea import Tarea

app=Flask(__name__)
ruta=os.getcwd()

Estudiantes= ArbolEstudiantes()
Pensum=ArbolCursos()
@app.route("/",methods=["GET"])
def inicio():
    return jsonify({"mensaje":"Server levantado :)"})
    
@app.route("/carga", methods=["POST"])
def carga():
    datos=request.get_json()
    print(datos["tipo"])
    print(datos["path"])
    
    
    if datos["tipo"] =="estudiante" or datos["tipo"]=="recordatorio":
        archivo = open(datos["path"],"r",encoding="utf-8")
        mensaje = archivo.read()
        parser.parse(mensaje)
        archivo.close()
        temp = usuarios_Lista.Primero
        while temp is not None:
            estudiante1 = Estudiante(temp.carnet, temp.dpi, temp.nombre, temp.carrera, temp.password, temp.creditos, temp.edad, temp.correo)
            Estudiantes.insertar(estudiante1)
            temp = temp.next 

        temp = tareas_Lista.Primero
        while temp is not None:
                mes1=temp.fecha[2:5]
                mes2=mes1.replace('/','')
                dia1=temp.fecha[0:2]
                dia2=dia1.replace('/','')
                año1=temp.fecha[6:10]
                año2=año1.replace('/','')
                hora1=temp.hora[0:2]
                hora2=hora1.replace(':','')
                tarea1 = Tarea(temp.nombre,temp.carnet,temp.descripcion,temp.materia,temp.fecha,temp.hora,temp.Estado,int(mes2),int(dia2))
                Estudiantes.cargarTarea(temp.carnet,int(año2),int(mes2),int(hora2),int(dia2),tarea1)
                temp = temp.next
    elif datos["tipo"] =="curso":
        with open(datos["path"],"r",encoding="utf-8") as file:
            data = json.load(file)
            for i in data["Estudiantes"]:
                for j in i["Años"]:
                    for k in j["Semestres"]:
                        for l in k["Cursos"]:
                            curso1 = Curso(int(l["Codigo"]), l["Nombre"], l["Creditos"], l["Prerequisitos"], l["Obligatorio"])
                            Estudiantes.cargarCurso(i["Carnet"],int(j["Año"]),int(k["Semestre"]), curso1)

    return jsonify({"mensaje":"Archivo leido :)"})

@app.route("/cursosEstudiante", methods=["POST"])
def cargaCursos():
    datos=request.get_json()
    for i in datos["Estudiantes"]:
        for j in i["Años"]:
            for k in j["Semestres"]:
                for l in k["Cursos"]:
                    curso1 = Curso(int(l["Codigo"]), l["Nombre"], l["Creditos"], l["Prerequisitos"], l["Obligatorio"])
                    Estudiantes.cargarCurso(i["Carnet"],int(j["Año"]),int(k["Semestre"]), curso1)

    return jsonify({"mensaje":"Json leido :)"})


@app.route("/cursosPensum", methods=["POST"])
def cargaPensum():
    datos=request.get_json()
    for i in datos["Cursos"]:
        curso1=Curso(int(i["Codigo"]), i["Nombre"], i["Creditos"], i["Prerequisitos"], i["Obligatorio"])
        Pensum.InsertarDatos(int(i["Codigo"]), curso1)
    return jsonify({"mensaje":"Json leido :)"})

@app.route("/reporte", methods=["POST"])
def graficar():
    respuesta=""
    datos=request.get_json()
    if datos["tipo"]==0:
        Estudiantes.graficar()
        respuesta="Arbol generado"
    elif datos["tipo"]==1:
        respuesta=Estudiantes.graficarMatriz(datos["carnet"],int(datos["año"]), int(datos["mes"]))
    elif datos["tipo"]==2:
        respuesta=Estudiantes.graficarLista(datos["carnet"], int(datos["año"]), int(datos["mes"]),int(datos["dia"]), int(datos["hora"]))
    elif datos["tipo"]==3:
        respuesta = Pensum.Graficar("Pensum")

    return jsonify({"Mensaje":respuesta})    

if __name__ == "__main__":
    app.run(port=3000)    

#"path":"C:\\Users\\steve\\Desktop\\EDD\\EDD_SmartClass_201903974\\EDD_SmartClass_201903974\\Fase2\\codigo.txt"
#"path":"C:\\Users\\steve\\Desktop\\EDD\\EDD_SmartClass_201903974\\EDD_SmartClass_201903974\\Fase2\\Cursos.json"
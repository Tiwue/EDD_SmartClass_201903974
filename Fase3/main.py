
from re import template
import re

from flask.wrappers import JSONMixin
from Estructuras.ArbolCursos import ArbolCursos
from flask import Flask, json, request, jsonify,session, redirect,render_template,url_for,make_response,Response,send_file,send_from_directory
import os
from flask_cors import CORS
from analizador.sintactico import parser
from analizador.sintactico import usuarios_Lista, tareas_Lista
from Estructuras.ArbolEstudiantes import ArbolEstudiantes
from Estructuras.Estudiante import Estudiante
from Estructuras.Curso import Curso
from Estructuras.Tarea import Tarea
from Estructuras.Apunte import Apunte
from Estructuras.TablaHash import tablaHash
from cryptography.fernet import Fernet
import hashlib
import base64
app=Flask(__name__, static_url_path='/static')
CORS(app)

ruta=os.getcwd()
app.secret_key = b'asjdlfajsdf'
key=Fernet.generate_key()
f=Fernet(key)
Estudiantes= ArbolEstudiantes()
Pensum=ArbolCursos()
Apuntes= tablaHash()


def encriptarCadena(cadena):
    cadena1=f.encrypt(cadena.encode())
    return cadena1

def encriptarPassword(cadena):
    password=hashlib.sha256(cadena.encode())
    password1=password.hexdigest()
    password2=f.encrypt(password1.encode())
    return password2

def desencriptar(cadena):
    cadena1= f.decrypt(cadena).decode()
    return cadena1


@app.route("/",methods=["GET"])
def inicio():
    return redirect('home')

@app.route('/home', methods=['GET'])
def home():
    if 'user' in session:
        user=session['user']
        permisos=session['nivel']
        return render_template('home.html', usuario=session['user'], nivel=permisos)
    else:    
        return redirect("login")


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
    elif datos["tipo"]==4:
        respuesta=Estudiantes.graficarCursos(datos["carnet"], int(datos["año"]), int(datos["semestre"]),"Estudiante")    
    else:
        respuesta="Tipo de reporte no valido"
    return jsonify({"Mensaje":respuesta})    

@app.route("/estudiante", methods=["POST","GET","PUT","DELETE"])
def crudEstudiante():
    respuesta=""
    if request.method=="POST":
        datos=request.get_json()
        estudiante1=Estudiante(datos["carnet"],datos["DPI"],datos["nombre"],datos["carrera"],datos["password"],datos["creditos"],int(datos["edad"]), datos["correo"])
        Estudiantes.insertar(estudiante1)
        respuesta="Estudiante agragado con exito :)"
        return jsonify({"Mensaje":respuesta}) 
    elif request.method=="GET":
        datos=request.get_json()
        e1=Estudiantes.buscar(datos["carnet"]).estudiante
        if e1 != None:
            return jsonify({"Carnet":e1.carnet,"DPI":e1.dpi,"Nombre":e1.nombre,"Carrera":e1.carrera,"Password":e1.password,"Creditos":e1.creditos,"Edad":e1.edad,"Correo":e1.correo})
        else:
            return jsonify({"Mensaje":"No se encontró el estudiante"})
    elif request.method=="PUT":
        datos=request.get_json()
        respuesta=Estudiantes.modificar(datos["carnet"],datos["DPI"],datos["nombre"],datos["carrera"],datos["correo"],datos["password"],datos["creditos"],datos["edad"])
        return jsonify({"Mensaje":respuesta})
    elif request.method=="DELETE":
        datos=request.get_json()
        respuesta=Estudiantes.eliminar(datos["carnet"])
        return jsonify({"Mensaje":respuesta})
           
@app.route("/recordatorios",methods=["POST"])
def crudRecordatorio():
    if request.method=="POST":
        datos=request.get_json()
        mes1=datos["Fecha"][2:5]
        mes2=mes1.replace('/','')
        dia1=datos["Fecha"][0:2]
        dia2=dia1.replace('/','')
        año1=datos["Fecha"][6:10]
        año2=año1.replace('/','')
        hora1=datos["Hora"][0:2]
        hora2=hora1.replace(':','')
        tarea1 = Tarea(datos["Nombre"],datos["Carnet"],datos["Descripcion"],datos["Materia"],datos["Fecha"],datos["Hora"],datos["Estado"],int(mes2),int(dia2))
        Estudiantes.cargarTarea(datos["Carnet"],int(año2),int(mes2),int(hora2),int(dia2),tarea1)
        return jsonify({"Mensaje":"recordatorio cargado"}) 

@app.route("/login", methods=['POST','GET'])
def login():  
    if request.method=='POST':
        user=request.form['user'] 
        contrasenia=request.form['password']
        
        if str(user)=="admin" and str(contrasenia)=="admin":
            
            session['user'] = "admin"
            session['auth'] = 1
            session['nivel']="admin"
            print("sesion iniciada")
            
            return redirect('home')
        else:
            usuario=Estudiantes.buscar(str(user))
            if usuario!=None:
                contra=usuario.estudiante.password
                contra1=desencriptar(contra)
                
                cadena= str(contrasenia)
                password=encriptarPassword(cadena)
                contra2=desencriptar(password)
                
                if contra1==contra2:
                    
                    session['user']=usuario.estudiante.carnet
                    session['auth']=1
                    session['nivel']="estudiante"
                    op=0
                    return redirect('home')
                else:
                    session.clear()
                    session['user'] = "unknown"
                    session['auth'] = 0
                    return render_template("login.html",mensaje="Credenciales incorrectas")
            else:
                return render_template("login.html",mensaje="Usuario no registrado en el sistema")       
    else:
        return render_template("login.html",mensaje=None)    

@app.route("/register", methods=['POST','GET'])
def registro():
    if request.method=='POST':
        carnet=str(request.form['carnet'])
        dpi=encriptarCadena(str(request.form['dpi']))
        nombre=encriptarCadena(request.form['nombre'])
        carrera=encriptarCadena(request.form['carrera'])
        correo=encriptarCadena(request.form['correo'])
        contrasenia=encriptarPassword(str(request.form['password']))
        edad=encriptarCadena(str(request.form['edad']))
        creditos=encriptarCadena(str(request.form['creditos']))
        estudiane1=Estudiante(carnet,dpi,nombre,carrera,contrasenia,creditos,edad,correo)
        Estudiantes.insertar(estudiane1)
        return render_template('register.html', mensaje="Usuario creado") 
    else:
        return render_template('register.html', mensaje=None) 

@app.route("/apuntes", methods=['POST','GET'])
def apuntes():
    if request.method=='POST':
        
        carnet=session['user']
        apunts=Apuntes.getApuntes(int(carnet))
        id=len(apunts)+1
        titulo=request.form['titulo']
        apunte=request.form['apunte']
        Apuntes.insert_value(carnet,Apunte(id,carnet,titulo,apunte))
        apunts=Apuntes.getApuntes(int(carnet))
        return render_template('apuntes.html', usuario=session['user'], nivel=session['nivel'], apuntes=apunts)
    else:
        carnet=session['user']
        apunts=Apuntes.getApuntes(int(carnet))

        return render_template('apuntes.html', usuario=session['user'], nivel=session['nivel'], apuntes=apunts)    

@app.route('/apunte/<int:id>')
def note(id):
    apun= Apuntes.getApunte(int(session['user']),id)
    usuario=session['user']
    titulo=apun.titulo
    apunte=apun.apunte

    return render_template('apunte.html', usuario=usuario,titulo=titulo,informacion=apunte )

@app.route('/apunte/apuntes')
def backApun():
    return redirect(url_for('home'))

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('user', None)
    return redirect('login')

@app.route('/cargaEstudiantes', methods=['POST', 'GET'])  
def carga1():
    return render_template('cargaEstudiantes.html', mensaje=None)      

@app.route('/cargarEstudiantes', methods=['POST'])
def agregarRecetas():
    datos = request.get_json()
    contenido = base64.b64decode(datos['data']).decode('utf-8')
    msg=""
    try:
        data= json.loads(contenido)
        for i in data["estudiantes"]:
            carnet= str(i["carnet"])
            dpi=encriptarCadena(str(i["dpi"]))
            nombre= encriptarCadena(str(i["nombre"]))
            carrera=encriptarCadena(str(i["carrera"]))
            correo=encriptarCadena(str(i["correo"]))
            password=encriptarPassword(str(i["password"]))
            edad=encriptarCadena(str(i["edad"]))
            creditos=encriptarCadena(str(i["creditos"]))
            estu= Estudiante(carnet,dpi,nombre,carrera,password,creditos,edad,correo)
            Estudiantes.insertar(estu)
        msg="Usuarios Agregados"    
    except:
        msg="No se pudieron cargar los datos, ocurrio un error"
    return jsonify({"msg": msg})


@app.route("/cursosPensum", methods=["POST"])
def cargaPensum():
        datos=request.get_json()
        contenido = base64.b64decode(datos['data']).decode('utf-8')
        msg=""
        try:
            data= json.loads(contenido)
            for i in data["Cursos"]:
                curso1=Curso(str(i["Codigo"]), i["Nombre"], i["Creditos"], i["Prerequisitos"], i["Obligatorio"])
                Pensum.insertar(curso1)
            msg="Cursos cargados con exito"
        except:
            msg="No se pudieron cargar los cursos, ocurrió un error"
        return jsonify({"msg": msg})

@app.route('/cargaCursos', methods=['POST', 'GET'])  
def carga3():
    return render_template('cargaCursos.html', mensaje=None)

@app.route("/cargaApuntes", methods=["POST"])
def cargaPensum2():
        datos=request.get_json()
        contenido = base64.b64decode(datos['data']).decode('utf-8')
        msg=""
        try:
            data= json.loads(contenido)
            for i in data["usuarios"]:
                carnet=i["carnet"]
                for j in i["apuntes"]:
                    apunts=Apuntes.getApuntes(int(carnet))
                    id=len(apunts)+1
                    titulo=j["titulo"]
                    texto=j["contenido"]
                    apunte=Apunte(id,carnet,titulo,texto)
                    Apuntes.insert_value(carnet, apunte)
            msg="Apuntes cargados con exito"
        except:
            msg="No se pudieron cargar los apuntes, ocurrió un error"
        return jsonify({"msg": msg})

@app.route('/CargaApuntes', methods=['POST', 'GET'])  
def carga2():
    return render_template('cargaApuntes.html', mensaje=None)     

@app.route("/cargaCursosS", methods=["POST"])
def cargaCursos3():
        datos=request.get_json()
        contenido = base64.b64decode(datos['data']).decode('utf-8')
        msg=""
        try:
            data= json.loads(contenido)
            for i in data["Estudiantes"]:
                for j in i["Años"]:
                    for k in j["Semestres"]:
                        for l in k["Cursos"]:
                            curso1 = Curso(str(l["Codigo"]), l["Nombre"], l["Creditos"], l["Prerequisitos"], l["Obligatorio"])
                            Estudiantes.cargarCurso(i["Carnet"],int(j["Año"]),int(k["Semestre"]), curso1)
            msg="Cursos cargados con exito"
        except:
            msg="No se pudieron cargar los cursos, ocurrió un error"
        return jsonify({"msg": msg})

@app.route('/CargaCursosS', methods=['POST', 'GET'])  
def carga4():
    return render_template('cargaCursosS.html', mensaje=None)    

@app.route("/reporteEstudiantes")
def reporte1():
    Estudiantes.graficarEncriptado()
    return render_template('reporte1.html')


if __name__ == "__main__":
    app.run(port=3000)    


#"path":"C:\\Users\\steve\\Desktop\\Estudiantes.txt"
#"path":"C:\\Users\\steve\\Desktop\\EDD\\EDD_SmartClass_201903974\\EDD_SmartClass_201903974\\Fase2\\Cursos.json"





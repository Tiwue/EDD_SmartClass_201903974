#include <iostream>

#include <stdio.h>
#include <locale.h>
#include <wchar.h>
#include <string>
#include <fstream>
#include <sstream>
#include "ListaEstudiantes.cpp"
#include "Cola.cpp"
#include "ListaTareas.cpp"
using namespace std;
#include <regex>

void menuUsuarios();
void menuTareas();
void ingresoManual();
void lecturaUsuarios(string ruta_);
void lecturaTareas(string ruta_);
bool validarCorreo(string correo_);
void ingresoEstudiante();
void modificarEstudiante();
void menuCola();
void inicializarMatriz();
void lecturaTareas(string ruta_);
bool validarFecha(string fecha_);
void linealizar();
void reportes();
void codigoSalida();
Tarea matriztareas[5][30][9];
ListaEstudiantes *lista1 = new ListaEstudiantes();
ListaTareas *lista2 = new ListaTareas();
Cola *colaErrores = new Cola();
int idError=0;
int main(){
   setlocale(LC_ALL,"");
    inicializarMatriz();
    bool on= 1;
    
    do{
        int eleccion = 0;
        string ruta1="";
        string ruta2="";
        
        cout<<"\n     MENU PRINCIPAL\n"<< endl;
        cout << "1.Carga de Usuarios \n2.Carga de Tareas \n3.Ingreso Manual\n4.Reportes\n5.Salir" <<endl;
        cout << "\nEliga una opción:" << endl;
        cin >> eleccion;
        system("cls");
        
        switch ( eleccion){
            case 1:
                cout<<"Ingrese la ruta del archivo de Usuarios:"<<endl;
                cin >> ruta1;
                lecturaUsuarios(ruta1);
                cout<<"Archivo leido con exito"<<endl;
            break;
            case 2:
            cout<<"Ingrese la ruta del archivo de Tareas:"<<endl;
            cin >> ruta2;
            lecturaTareas(ruta2);
            cout<<"Archivo leido con exito"<<endl;
            break;
            case 3:
            ingresoManual();
            break;
            case 4:
            reportes();
            break;   
            case 5:
            on=0;
            break;  
            case 6:
            lista2->imprimir();
            break;
            case 7:
            lista1->imprimir();
            break;
            default:
            cout<<"Debe seleccionar una opcion correcta. Intente nuevamente"<<endl;
            break;
        }
    }
    while(on != 0);

    return 0;
};

void ingresarEstudiante(){
    string carnet, dpi, nombre, carrera, password, creditos, edad, correo;
    cout<<"Ingrese el nombre del estudiante:"<<endl;
    cin.ignore();
    getline(cin, nombre);
    cout<<"Ingrese el carnet:"<<endl;
    cin>>carnet;
    cout<<"Ingrese el DPI del estudiante:"<<endl;
    cin>>dpi;
    cout<<"Ingrese la carrera del estudiante:"<<endl;
    cin.ignore();
    getline(cin, carrera);
    cout<<"Ingrese los creditos aprobados del estudiante:"<<endl;
    cin>>creditos;
    cout<<"Ingrese la edad del estudiante:"<<endl;
    cin>>edad;
    cout<<"Ingrese el correo del estudiante:"<<endl;
    cin>>correo;
    cout<<"Ingrese la contraseña del estudiante:"<<endl;
    cin.ignore();
    getline(cin, password);

    Estudiante e1(nombre, stoi(edad), carnet, dpi, stoi(creditos), carrera, correo, password);

    if(carnet.size()!= 9){
        idError++;
        Error e1= Error(idError,"Estudiante", "El carnet del estudiante no cumple con 9 caracteres",dpi);
        colaErrores->encolar(e1);
        cout<<"Error en el carnet"<<endl;
    }

    if(dpi.size() != 13){
        idError++;
        Error e1= Error(idError,"Estudiante", "El DPI del estudiante no cumple con 13 caracteres",dpi);
        colaErrores->encolar(e1);
        cout<<"Error en el dpi"<<endl;
    }
    if(validarCorreo(correo)){
    }else{
        idError++;
        Error e1= Error(idError,"Estudiante", "El correo del estudiante no cumple con el formato correcto dado",dpi);
        colaErrores->encolar(e1);
        cout<<"Error en el correo"<<endl;
    }

    lista1->insertar(e1);
}

void modificarEstudiante(){
    string carnet, dpi1, dpi2, nombre, carrera, password, creditos, edad, correo;

    cout<<"Ingrese el dpi del estudiante: "<<endl;
    cin>>dpi1;
    if(lista1->exist(dpi1)){
        Estudiante e1 = lista1->searchEstudiante(dpi1);
        
        cout<<"\n   Eliga el campo que desea modificar:\n1.Nombre\n2.Carnet\n3.DPI\n4.Edad\n5.Carrera\n6.Correo\n7.Password\n8.Creditos\n9.Cancelar"<<endl;
        int opcion =0;
        cin>>opcion;
        switch (opcion)
        {
        case 1:
            cout<<"Ingrese el nombre nuevo:"<<endl;
            cin>>nombre;
            e1.setNombre(nombre);
            lista1->modificar(dpi1, e1);
            break;
        case 2:
            cout<<"Ingrese el carnet nuevo:"<<endl;
            cin>>carnet;
            e1.setCarnet(carnet);

            if(carnet.size()!= 9){
                idError++;
                Error e1= Error(idError,"Estudiante", "El carnet del estudiante no cumple con 9 caracteres",dpi1);
                colaErrores->encolar(e1);
                cout<<"Error en el carnet"<<endl;
            }

            lista1->modificar(dpi1, e1);
            break;
        case 3:
            cout<<"Ingrese el DPI nuevo:"<<endl;
            cin>>dpi2;
            e1.setDpi(dpi2);
            if(dpi2.size() != 13){
            idError++;
            Error e1= Error(idError,"Estudiante", "El DPI del estudiante no cumple con 13 caracteres",dpi2);
            colaErrores->encolar(e1);
            cout<<"Error en el dpi"<<endl;
            }
            lista1->modificar(dpi1, e1);
            break;
        case 4:
            cout<<"Ingrese la edad nueva:"<<endl;
            cin>>edad;
            e1.setEdad(stoi(edad));
            lista1->modificar(dpi1, e1);
            break;
        case 5:
            cout<<"Ingrese la Carrera nueva:"<<endl;
            cin.ignore();
            getline(cin, carrera);
            e1.setCarrera(carrera);
            lista1->modificar(dpi1, e1);
            break;
        case 6:
            cout<<"Ingrese el correo nuevo:"<<endl;
            cin>>correo;
            e1.setCorreo(correo);
            if(validarCorreo(correo)){
            }else{
            idError++;
            Error e1= Error(idError,"Estudiante", "El correo del estudiante no cumple con el formato dado correcto",dpi1);
            colaErrores->encolar(e1);
            cout<<"Error en el correo"<<endl;
            }
            lista1->modificar(dpi1, e1);
            break;
        case 7:
            cout<<"Ingrese la contraseña nueva:"<<endl;
            cin>>password;
            e1.setPassword(password);
            lista1->modificar(dpi1, e1);
            break;
        case 8:
            cout<<"Ingrese los creditos nuevos:"<<endl;
            cin>>creditos;
            e1.setCreditos(stoi(creditos));
            lista1->modificar(dpi1, e1);
            break;
        default:
            break;
        }
    }else{
        cout<<"No se encontro un estudiante registrado con el siguiente dpi: "<<dpi1<<endl;
    }

}

void modificarTarea(){
    string m, d, h, carnet, nombre, descripcion, materia, fecha, estado,horaS;
    int i,j,k, mes, dia, hora,id1,id2;
    bool agregar=true;

    cout<<"Ingrese el id de la tarea: "<<endl;
    cin>>id1;
    if(lista2->exist(to_string(id1))){
        Tarea e1 = lista2->searchTarea(to_string(id1));
        
        cout<<"\n   Eliga el campo que desea modificar:\n1.Nombre\n2.Carnet\n3.Descripcion\n4.Materia\n5.Mes\n6.Dia\n7.Hora\n8.Estado\n9.Cancelar"<<endl;
        int opcion =0;
        cin>>opcion;
        switch (opcion)
        {
        case 1:
            cout<<"Ingrese el nombre nuevo:"<<endl;
            cin.ignore();
            getline(cin,nombre);
            e1.setNombre(nombre);
            lista2->modificar(to_string(id1), e1);
            break;
        case 2:
            cout<<"Ingrese el carnet nuevo:"<<endl;
            cin>>carnet;
            e1.setCarnet(carnet);

            if(carnet.size()!= 9){
                idError++;
                Error e2= Error(idError,"Estudiante", "El carnet del estudiante no cumple con 9 caracteres",to_string(id1));
                colaErrores->encolar(e2);
                cout<<"Error en el carnet"<<endl;
            }

            lista2->modificar(to_string(id1), e1);
            break;
        case 3:
            cout<<"Ingrese la descripción nueva:"<<endl;
            cin.ignore();
            getline(cin,descripcion);
            e1.setDescripcion(to_string(id1));
            lista2->modificar(to_string(id1), e1);
            break;
        case 4:
            cout<<"Ingrese la materia nueva:"<<endl;
            cin.ignore();
            getline(cin,materia);
            e1.setMateria(materia);
            lista2->modificar(to_string(id1), e1);
            break;
        case 5:
            cout<<"Ingrese el nuevo mes de entrega:"<<endl;
            cin>>mes;
            if(mes>6 && mes<12){
            i=mes-7;
            j=e1.getDia();
            k=e1.getHora();
            dia=e1.getDia()+1;
            id2=k+9*(j+30*i);
            if(lista2->exist(to_string(id2))){
                 idError++;
                Error e2= Error(idError,"Tarea", "Ya existe una tarea registrada en el mismo horario, no se pudo agregar",to_string(id1));
                colaErrores->encolar(e2);
                cout<<"Error horario ya se encuentra ocupado"<<endl;

            }else{
            e1.setMes(i);
            e1.setId(id2);
            if(to_string(mes).length()==1){
                fecha="2021/0"+to_string(mes)+"/";
            }else{
            fecha="2021/"+to_string(mes)+"/";
            }

            if(to_string(dia).length()==1){
            fecha.append("0"+to_string(dia));
            }else{
            fecha.append(to_string(dia));
            }
            e1.setFechaS(fecha);
            
            lista2->modificar(to_string(id2), e1);
            lista2->eliminar(to_string(id1));
            }
            }else{
                idError++;
            Error e2= Error(idError,"Tarea", "El mes indicado en la modificacion no es permitido en el rango establecido",to_string(id1));
            colaErrores->encolar(e2);
            cout<<"Error en el mes"<<endl;
            }
            break;
        case 6:
            cout<<"Ingrese el nuevo dia de entrega:"<<endl;
            cin>>dia;
            if(dia>0 && dia<31){
            i=e1.getMes();
            j=dia-1;
            k=e1.getHora();
            id2=k+9*(j+30*i);
            mes=e1.getMes()+7;
            if(lista2->exist(to_string(id2))){
                 idError++;
                Error e2= Error(idError,"Tarea", "Ya existe una tarea registrada en el mismo horario, no se pudo agregar",to_string(id1));
                colaErrores->encolar(e2);
                cout<<"Error horario ya se encuentra ocupado"<<endl;

            }else{
            e1.setDia(j);
            e1.setId(id2);
            if(to_string(mes).size()==1){
                fecha="2021/0"+to_string(mes)+"/";
            }else{
            fecha="2021/"+to_string(mes)+"/";
            }

            if(to_string(dia).size()==1){
            fecha.append("0"+to_string(dia));
            }else{
            fecha.append(to_string(dia));
            }
            e1.setFechaS(fecha);
            lista2->modificar(to_string(id2), e1);
            lista2->eliminar(to_string(id1));
            }
            }else{
            idError++;
            Error e2= Error(idError,"Tarea", "El dia indicado en la modificacion no es permitido en el rango establecido",to_string(id1));
            colaErrores->encolar(e2);
            cout<<"Error en el mes"<<endl;

            }
            break;
        case 7:

            cout<<"Ingrese la nueva hora de entrega:"<<endl;
            cin>>hora;
            if(hora>7 && hora<17){
            i=e1.getMes();
            j=e1.getDia();
            k=hora-8;
            id2=k+9*(j+30*i);
            if(lista2->exist(to_string(id2))){
                 idError++;
                Error error= Error(idError,"Tarea", "Ya existe una tarea registrada en el mismo horario, no se pudo agregar",to_string(id1));
                colaErrores->encolar(error);
                cout<<"Error horario ya se encuentra ocupado"<<endl;
            }else{
            e1.setHora(k);
            e1.setId(id2);
            horaS=to_string(hora)+":00";
            
            e1.setHoraS(horaS);
            lista2->modificar(to_string(id2), e1);
            lista2->eliminar(to_string(id1));
            };
            }else{
            idError++;
            cout<<"Error en el mes"<<endl;
            Error e2= Error(idError,"Tarea", "La hora indicada en la modificacion no es permitida en el rango establecido",to_string(id1));
            colaErrores->encolar(e2);
            
            }
            break;
        case 8:
            cout<<"Ingrese el estado nuevo:"<<endl;
            cin>>estado;
            e1.setEstado(estado);
            lista2->modificar(to_string(id1), e1);
            break;
        default:
            break;
        }
    }else{
        cout<<"No se encontro un estudiante registrado con el siguiente dpi: "<<id1<<endl;
    }

}

void menuUsuarios(){
    bool on=1;
    do{
        int eleccion=0;
        cout<<"\n   MENU USUARIOS\n"<<endl;
        cout << "1.Agregar \n2.Modificar \n3.Eliminar \n4.Regresar" <<endl;
        cout << "\nEliga una opción:" << endl;
        cin >> eleccion;
        int confirmacion;
        system("cls");
        string dpi;
        switch ( eleccion){
            case 1:
                ingresarEstudiante();
                
            break;
            case 2:
                modificarEstudiante();
            break;
            case 3:
            cout<<"Ingrese el dpi del estudiante que desea eliminar:"<<endl;
            cin.ignore();
            getline(cin, dpi);
            cout<<"Esta seguro de eliminar a este estudiante: \n1.Confirmar\n2.Cancelar"<<endl;
            
            cin>>confirmacion;
            if (confirmacion == 1){
                lista1->eliminar(dpi);
            }if (confirmacion!=0 && confirmacion !=1){
                cout<<"No eligió un valor correcto"<<endl;
            }
            break;    
            case 4:
            
            on=0;
            break;    
            default:
            cout<<"Debe seleccionar una opcion correcta. Intente nuevamente"<<endl;
        }
    }while(on != 0);
}

void ingresarTarea(){
    string mes, dia, hora, carnet, nombre, descripcion, materia, fecha, estado,horaS;
    int i,j,k,id;
    bool agregar=true;
    cout<<"Ingrese el nombre de la tarea:"<<endl;
    cin.ignore();
    getline(cin, nombre);
    cout<<"Ingrese el carnet:"<<endl;
    cin>>carnet;
    cout<<"Ingrese la descripcion de la tarea:"<<endl;
    cin.ignore();
    getline(cin, descripcion);
    cout<<"Ingrese la materia de la tarea:"<<endl;
    cin.ignore();
    getline(cin, materia);
    cout<<"Ingrese el mes de entrega:"<<endl;
    cin>>mes;
    cout<<"Ingrese el dia de entrega:"<<endl;
    cin>>dia;
    cout<<"Ingrese la hora de entrega:"<<endl;
    cin>>hora;
    cout<<"Ingrese el estado de la tarea:"<<endl;
    cin.ignore();
    getline(cin, estado);
    if(mes.size()==1){
        fecha="2021/0"+mes+"/";
    }else{
        fecha="2021/"+mes+"/";
    }

    if(dia.size()==1){
        fecha.append("0"+dia);
    }else{
        fecha.append(dia);
    }
    horaS=hora.append(":00");
    i=stoi(mes)-7;
    j=stoi(dia)-1;
    k=stoi(hora)-8;
    id=k+9*(j+30*i);

    Tarea t1(id,nombre,carnet,descripcion,materia,horaS,fecha,estado,i,j,k);

    if(carnet.size()!= 9){
        idError++;
        Error e1= Error(idError,"Tarea", "El carnet del estudiante no cumple con 9 caracteres",to_string(id));
        colaErrores->encolar(e1);
        cout<<"Error en el carnet"<<endl;
    }

    if(stoi(mes) < 7 || stoi(mes)>11){
        idError++;
        Error e1= Error(idError,"Tarea", "El mes indicado no es permitido en el rango establecido",to_string(id));
        colaErrores->encolar(e1);
        cout<<"Error en el mes"<<endl;
        agregar=false;
    }

    if(stoi(dia) < 1 || stoi(dia)>30){
        idError++;
        Error e1= Error(idError,"Tarea", "El dia indicado no es permitido en el rango establecido",to_string(id));
        colaErrores->encolar(e1);
        cout<<"Error en el dia"<<endl;
        agregar=false;
    }

    if(stoi(hora) < 8 || stoi(hora)>16){
        idError++;
        Error e1= Error(idError,"Tarea", "La hora indicada no es permitida en el rango establecido",to_string(id));
        colaErrores->encolar(e1);
        cout<<"Error en la hora"<<endl;
        agregar=false;
    }

    if(validarFecha(fecha)){
    }else{
        idError++;
        Error e1= Error(idError,"Tarea", "La fecha no cumple con el formato dado correcto",to_string(id));
        colaErrores->encolar(e1);
        cout<<"Error en la fecha"<<endl;
    }

    if(lista1->carnetExist(carnet)){
    }else{
        idError++;
        Error e1= Error(idError,"Tarea", "No existe un estudiante registrado con este carnet",to_string(id));
        colaErrores->encolar(e1);
        cout<<"Error no se encontro carnet"<<endl;
    }

        if(agregar==true){
            if(lista2->exist(to_string(id))){
                idError++;
                Error e1= Error(idError,"Tarea", "Ya existe una tarea registrada en el mismo horario, no se pudo agregar",to_string(id));
                colaErrores->encolar(e1);
                cout<<"Error horario ya se encuentra ocupado"<<endl;
            }else{
                lista2->modificar(to_string(id),t1);
            }
    }
}


void menuTareas(){
    bool on=1;
    do{
        int eleccion=0;
        cout<<"\n   MENU TAREAS\n"<<endl;
        cout << "1.Agregar \n2.Modificar \n3.Eliminar \n4.Regresar" <<endl;
        cout << "\nEliga una opción:" << endl;
        cin >> eleccion;
        system("cls");
        string id;
        int confirmacion;
        switch ( eleccion){
            case 1:
                ingresarTarea();
            break;
            case 2:
            modificarTarea();
            break;
            case 3:
            cout<<"Ingrese el id de la tarea que desea eliminar:"<<endl;
            cin.ignore();
            getline(cin, id);
            cout<<"Esta seguro de eliminar a esta tarea: \n1.Confirmar\n2.Cancelar"<<endl;
            cin>>confirmacion;
            if (confirmacion == 1){
                lista2->eliminar(id);
            }if (confirmacion!=0 && confirmacion !=1){
                cout<<"No eligió un valor correcto"<<endl;
            }
            break;       
            case 4:
            on=0;
            break;    
            default:
            cout<<"Debe seleccionar una opcion correcta. Intente nuevamente"<<endl;
        }
    }while(on != 0);
}

void ingresoManual(){
    bool on=1;
    do{
        int eleccion=0;
        cout<<"\n   INGRESO MANUAL\n"<<endl;
        cout << "1.Usuarios \n2.Tareas \n3.Regresar" <<endl;
        cout << "\nEliga una opción:" << endl;
        cin >> eleccion;
        system("cls");

        switch ( eleccion){
            case 1:
                menuUsuarios();
            break;
            case 2:
                menuTareas();
            break;
            case 3:
            on=0;
            break;        
            default:
            cout<<"Debe seleccionar una opcion correcta. Intente nuevamente"<<endl;
        }
    }while(on != 0);
}

void lecturaUsuarios(string ruta_){
    ifstream archivo(ruta_);
    string linea;
    char delimitador = ',';
    getline(archivo, linea);
    while (getline(archivo, linea))
    {
    stringstream stream(linea); // Convertir la cadena a un stream
    string carnet, dpi, nombre, carrera, password, creditos, edad, correo;
    getline(stream, carnet, delimitador);
    getline(stream, dpi, delimitador);
    getline(stream, nombre, delimitador);
    getline(stream, carrera, delimitador);
    getline(stream, password, delimitador);
    getline(stream, creditos, delimitador);
    getline(stream, edad, delimitador);
    getline(stream, correo, delimitador);
    Estudiante e1(nombre, stoi(edad), carnet, dpi, stoi(creditos), carrera, correo, password);

    if(carnet.size()!= 9){
        idError++;
        Error e1= Error(idError,"Estudiante", "El carnet del estudiante no cumple con 9 caracteres",dpi);
        colaErrores->encolar(e1);
        cout<<"Error en el carnet"<<endl;
    }

    if(dpi.size() != 13){
        idError++;
        Error e1= Error(idError,"Estudiante", "El carnet del DPI no cumple con 13 caracteres",dpi);
        colaErrores->encolar(e1);
        cout<<"Error en el dpi"<<endl;
    }
    if(validarCorreo(correo)){
    }else{
        idError++;
        Error e1= Error(idError,"Estudiante", "El correo electronico no cumple con el formato dado correcto",dpi);
        colaErrores->encolar(e1);
        cout<<"Error en el correo"<<endl;
    }

    lista1->insertar(e1);
    }
    archivo.close();
}

void lecturaTareas(string ruta_){
ifstream archivo(ruta_);
    string linea;
    char delimitador = ',';
    getline(archivo, linea);
    while (getline(archivo, linea))
    {
    stringstream stream(linea); // Convertir la cadena a un stream
    string mes, dia, hora, carnet, nombre, descripcion, materia, fecha, estado,horaS;
    int i,j,k,id;
    bool agregar=true;
    getline(stream, mes, delimitador);
    getline(stream, dia, delimitador);
    getline(stream, hora, delimitador);
    getline(stream, carnet, delimitador);
    getline(stream, nombre, delimitador);
    getline(stream, descripcion, delimitador);
    getline(stream, materia, delimitador);
    getline(stream, fecha, delimitador);
    getline(stream, estado, delimitador);
    i=stoi(mes)-7;
    j=stoi(dia)-1;
    k=stoi(hora)-8;
    id=k+9*(j+30*i);
    horaS=hora.append(":00");

    Tarea t1(id,nombre,carnet,descripcion,materia,horaS,fecha,estado,i,j,k);

    if(carnet.size()!= 9){
        idError++;
        Error e1= Error(idError,"Tarea", "El carnet del estudiante no cumple con 9 caracteres",to_string(id));
        colaErrores->encolar(e1);
        cout<<"Error en el carnet"<<endl;
    }

    if(stoi(mes) < 7 || stoi(mes)>11){
        idError++;
        Error e1= Error(idError,"Tarea", "El mes indicado no es permitido en el rango establecido",to_string(id));
        colaErrores->encolar(e1);
        cout<<"Error en el mes"<<endl;
        agregar=false;
    }

    if(stoi(dia) < 1 || stoi(dia)>30){
        idError++;
        Error e1= Error(idError,"Tarea", "El dia indicado no es permitido en el rango establecido",to_string(id));
        colaErrores->encolar(e1);
        cout<<"Error en el dia"<<endl;
        agregar=false;
    }

    if(stoi(hora) < 8 || stoi(hora)>16){
        idError++;
        Error e1= Error(idError,"Tarea", "La hora indicada no es permitida en el rango establecido",to_string(id));
        colaErrores->encolar(e1);
        cout<<"Error en la hora"<<endl;
        agregar=false;
    }

    if(validarFecha(fecha)){
    }else{
        idError++;
        Error e1= Error(idError,"Tarea", "La fecha no cumple con el formato dado correcto",to_string(id));
        colaErrores->encolar(e1);
        cout<<"Error en la fecha"<<endl;
    }

    if(lista1->carnetExist(carnet)){
    }else{
        idError++;
        Error e1= Error(idError,"Tarea", "No existe un estudiante registrado con este carnet",to_string(id));
        colaErrores->encolar(e1);
        cout<<"Error no se encontro carnet"<<endl;
    }

        if(agregar==true){
            if(matriztareas[i][j][k].getNombre()=="-1"){
            matriztareas[i][j][k]=t1;
            }else{
                idError++;
                Error e1= Error(idError,"Tarea", "Ya existe una tarea registrada en el mismo horario, no se pudo agregar",to_string(id));
                colaErrores->encolar(e1);
                cout<<"Error horario ya se encuentra ocupado"<<endl;
            }
    }
    }
    linealizar();
    archivo.close();
}

bool validarCorreo(string correo_){
    const regex expReg("[a-zA-Z0-9.]+@[a-zA-Z0-9]+\\.((com)|(es)|(org))");
    return regex_match(correo_, expReg);
}

bool validarFecha(string fecha_){
    const regex expReg("[0-9][0-9][0-9][0-9]/[0-9][0-9]/[0-9][0-9]");
    return regex_match(fecha_, expReg);
}

void menuCola(){


    bool on=1;
    do{
        int eleccion=0;
        cout<<"\n   COLA DE ERRORES\n"<<endl;
        cout << "1.Ver Cola \n2.Desencolar \n3.Imprimir en consola" <<endl;
        cout << "\nEliga una opción:" << endl;
        cin >> eleccion;
        int confirmacion;
        system("cls");
        string dpi;
        switch ( eleccion){
            case 1:
                if(colaErrores->isEmpty()){
                    cout<<"No hay errores en cola"<<endl;
                }else{
                colaErrores->graficar();
                }
            break;
            case 2:
                colaErrores->desencolar();
            break;
            case 3:
            colaErrores->recorrer();
            break;  
            case 4:
            on=0;  
            default:
            cout<<"Debe seleccionar una opcion correcta. Intente nuevamente"<<endl;
        }
    }while(on != 0);
}

void inicializarMatriz(){
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 30; j++)
        {
            for (int k = 0; k < 9; k++)
            {
                matriztareas[i][j][k]=  Tarea(k+9*(j+30*i),"-1","-1","-1","-1","-1","-1","-1",i,j,k);   
            }   
        }  
    }

    for(int i=0;i<1350;i++){
        lista2->insertar(Tarea(i,"-1","-1","-1","-1","-1","-1","-1",-1,-1,-1));
    }
    
}

void linealizar(){
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 30; j++)
        {
            for (int k = 0; k < 9; k++)
            {
                if(lista2->exist(to_string(k+9*(j+30*i)))){
                    idError++;
                    Error e1= Error(idError,"Tarea", "Ya existe una tarea registrada en el mismo horario, no se pudo agregar",to_string(k+9*(j+30*i)));
                    colaErrores->encolar(e1);
            }else{
                lista2->modificar(to_string(k+9*(j+30*i)), matriztareas[i][j][k]) ;   
            }
            }
            
        }
        
    }
    
}

void reportes(){
    bool on=1;
    do{
        int eleccion=0;
        cout<<"\n   MENU Reportes\n"<<endl;
        cout << "1.Lista Estudiantes \n2.Lista Tareas Linealizadas \n3.Busqueda en estructura linealizada \n4.Busqueda de Posicion en Estrucutura linealizada\n5.Cola de Errores\n6.Codigo de Salida\n7.Salir" <<endl;
        cout << "\nEliga una opción:" << endl;
        cin >> eleccion;
        int confirmacion;
        system("cls");
        string dpi;
        int mes, dia,hora,id;
        switch ( eleccion){
            case 1:
                if(colaErrores->isEmpty()){
                lista1->graficar();        
                }else{
                    cout<<"Hay errores en cola, debe arreglar primero antes de graficar"<<endl;
                }        
            break;
            case 2:
            if(colaErrores->isEmpty()){
               lista2->graficar();
            }else{
                cout<<"Hay errores en cola, debe arreglar primero antes de graficar"<<endl;
            }
            break;
            case 3:
            if(colaErrores->isEmpty()){
                cout<<"Ingrese el mes:"<<endl;
                cin>>mes;
                cout<<"Ingrese el dia:"<<endl;
                cin>>dia;
                cout<<"Ingrese la hora:"<<endl;
                cin>>hora;
                id=(hora-8)+9*((dia-1)+30*(mes-7));
                if(lista2->exist(to_string(id))){
                    Tarea t1=lista2->searchTarea(to_string(id));
                    cout<<"\nID: "<<t1.getId()<<endl;
                    cout<<"Nombre de la Tarea: "<<t1.getNombre()<<endl;
                    cout<<"Descripcion: "<<t1.getDescripcion()<<endl;
                    cout<<"Carnet: "<<t1.getCarnet()<<endl;
                    cout<<"Materia: "<<t1.getMateria()<<endl;
                    cout<<"Fecha: "<<t1.getFechaS()<<endl;
                    cout<<"Hora: "<<t1.getHoraS()<<endl;
                    cout<<"Estado: "<<t1.getEstado()<<endl;
                }else{
                    cout<<"No existe una tarea con estos parametros"<<endl;
                }
            }else{
                cout<<"Hay errores en cola, debe arreglar primero antes de graficar"<<endl;
            }
            break;    
            case 4:
             cout<<"Ingrese el mes:"<<endl;
                cin>>mes;
                cout<<"Ingrese el dia:"<<endl;
                cin>>dia;
                cout<<"Ingrese la hora:"<<endl;
                cin>>hora;
                id=(hora-8)+9*((dia-1)+30*(mes-7));
                cout<<"\nEl ID es: "<<to_string(id)<<endl;
            
            break;
            case 5:
            menuCola();
            break;
            case 6:
            codigoSalida();
            break;
            case 7:
            on=0;
            break;
                
            default:
            cout<<"Debe seleccionar una opcion correcta. Intente nuevamente"<<endl;
        }
    }while(on != 0);
}

void codigoSalida(){
    string texto="¿Elements?\n";
    texto=texto+lista1->generarCodigo();
    texto=texto+lista2->generarCodigo();
    texto=texto+"¿$Elements?";

        try{
        //Esta variable debe ser modificada para agregar su path de creacion de la Grafica

        ofstream file;
        file.open("codigo.txt",std::ios::out);

        file<<texto;
        file.close();
    }catch(exception e){
        cout<<"Fallo detectado"<<endl;
    }
    

}
/*C:\Users\steve\Desktop\Estudiantes.csv*/
/*C:\Users\steve\Desktop\Tareas.csv*/
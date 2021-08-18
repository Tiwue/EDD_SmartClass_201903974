#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <locale.h>
#include <wchar.h>
#include <string>
#include <fstream>
#include <sstream>
#include "ListaEstudiantes.cpp"
#include "Cola.cpp"

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

ListaEstudiantes *lista1 = new ListaEstudiantes();
Cola *colaErrores = new Cola();
int idError=0;
int main(){
   setlocale(LC_ALL,"");
    
    bool on= 1;
    
    do{
        int eleccion = 0;
        string ruta1="";
        string ruta2="";
        cout<<"\n     MENU PRINCIPAL\n"<< endl;
        cout << "1.Carga de Usuarios \n2.Carga de Tareas \n3.Ingreso Manual\n4.Reportes\n5.Salir\n6.ImprimirLista" <<endl;
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
            break;
            case 3:
            ingresoManual();
            break;
            case 4:
            cout<<"Reportes"<<endl;
            break;   
            case 5:
            on=0;   
            break;  
            case 6:
            lista1->imprimir();
            break;    
            default:
            cout<<"Debe seleccionar una opcion correcta. Intente nuevamente"<<endl;
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
        cout<<"Error en el carnet"<<endl;
    }

    if(dpi.size() != 13){
        cout<<"Error en el dpi"<<endl;
    }
    if(validarCorreo(correo)){
    }else{
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

void menuUsuarios(){
    bool on=1;
    do{
        int eleccion=0;
        cout<<"\n   MENU USUARIOS\n"<<endl;
        cout << "1.Agregar \n2.Modificar \n3.Eliminar \n4.Regresar" <<endl;
        cout << "\nEliga una opción:" << endl;
        cin >> eleccion;
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
            lista1->eliminar(dpi);
            break;    
            case 4:
            
            on=0;
            break;    
            default:
            cout<<"Debe seleccionar una opcion correcta. Intente nuevamente"<<endl;
        }
    }while(on != 0);
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

        switch ( eleccion){
            case 1:
                cout<<"Agregando Tarea"<<endl;
            break;
            case 2:
            cout<<"Modificando Tarea"<<endl;
            break;
            case 3:
            cout<<"Eliminando Tarea"<<endl;
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

bool validarCorreo(string correo_){
    const regex expReg("[a-zA-Z0-9.]+@[a-zA-Z0-9]+\\.((com)|(es)|(org))");
    return regex_match(correo_, expReg);
}

/*C:\Users\steve\Desktop\Estudiantes.csv*/
/*C:\Users\steve\Desktop\Tareas.csv*/
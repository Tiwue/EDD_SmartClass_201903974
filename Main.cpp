#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <locale.h>
#include <wchar.h>
#include <string>
using namespace std;


void menuUsuarios(){
    bool on=1;
    do{
        int eleccion=0;
        cout<<"\n   MENU USUARIOS\n"<<endl;
        cout << "1.Agregar \n2.Modificar \n3.Eliminar \n4.Regresar" <<endl;
        cout << "\nEliga una opción:" << endl;
        cin >> eleccion;
        system("cls");

        switch ( eleccion){
            case 1:
                cout<<"Agregando usuario"<<endl;
            break;
            case 2:
            cout<<"Modificando usuario"<<endl;
            break;
            case 3:
            cout<<"Eliminando usuarios"<<endl;
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


int main(){
   setlocale(LC_ALL,"");
    
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
            default:
            cout<<"Debe seleccionar una opcion correcta. Intente nuevamente"<<endl;
        }
    }
    while(on != 0);

    return 0;
}


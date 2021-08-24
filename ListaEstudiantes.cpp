#include "ListaEstudiantes.h"
#include <iostream>
#include <fstream>
using namespace std;
int index=0;
ListaEstudiantes::ListaEstudiantes(){

    this->inicio=NULL;
}

bool ListaEstudiantes::isEmpty(){

    return this->inicio==NULL;
}

int ListaEstudiantes::getSize(){

    NodoEstudiante *aux = this->inicio;
    int contador = 0;

    if(this->inicio!=NULL){
    contador++;
	aux=aux->getSiguiente();	
    while(aux !=this->inicio){
        contador++;
        aux = aux->getSiguiente();
        }
        return contador;
    }else{
        cout<<"La lista de estudiantes aun no tiene elementos"<<endl;
        return 0;
    }
}

void ListaEstudiantes::insertar(Estudiante estudiante_){

    NodoEstudiante *newNodo = new NodoEstudiante(estudiante_);
    if (isEmpty()){
        this->inicio=newNodo;
        this->inicio->setSiguiente(newNodo);
        this->inicio->setAnterior(newNodo);
    }else{
        NodoEstudiante *aux = this->inicio;
        while(aux->getSiguiente()!=this->inicio){
            aux=aux->getSiguiente();
        }
        aux->setSiguiente(newNodo);
        newNodo->setAnterior(aux);
        newNodo->setSiguiente(this->inicio);
        this->inicio->setAnterior(newNodo);
    }

}

void ListaEstudiantes::imprimir(){
    NodoEstudiante *aux = this->inicio;
    if(this->inicio!=NULL){
    aux->getEstudiante().toString();
	aux=aux->getSiguiente();	
    while(aux !=this->inicio){
        aux->getEstudiante().toString();
        aux = aux->getSiguiente();
        }
    }else{
        cout<<"La lista de estudiantes aun no tiene elementos"<<endl;
    }
}

Estudiante ListaEstudiantes::searchEstudiante(string dpi_){

    NodoEstudiante *aux = this->inicio;
    if(this->inicio!=NULL){
    if(aux->getEstudiante().getDpi()==dpi_){
        return aux->getEstudiante();
    }
	aux=aux->getSiguiente();	
    while(aux !=this->inicio){
            if(aux->getEstudiante().getDpi()==dpi_){
                return aux->getEstudiante();
            }
        aux = aux->getSiguiente();
        }
        cout<<"No existe ningun estudiante con este dpi"<<endl;
        
    }else{
       cout<< "La lista aun no tiene estudiantes"<<endl;
       
    }
}

bool ListaEstudiantes::exist(string dpi_){

    NodoEstudiante *aux = this->inicio;
    if(this->inicio!=NULL){
    if(aux->getEstudiante().getDpi()==dpi_){
        return true;
    }
	aux=aux->getSiguiente();	
    while(aux !=this->inicio){
            if(aux->getEstudiante().getDpi()==dpi_){
                return true;
            }
        aux = aux->getSiguiente();
        }
        return false;
    }else{
       return false;
    }
}

void ListaEstudiantes::modificar(string dpi_, Estudiante estudiante_){
    
    NodoEstudiante *aux = this->inicio;
    if(this->inicio!=NULL){
    if(aux->getEstudiante().getDpi()==dpi_){
        aux->setEstudiante(estudiante_);
        return;
    }
	aux=aux->getSiguiente();	
    while(aux !=this->inicio){
            if(aux->getEstudiante().getDpi()==dpi_){
                aux->setEstudiante(estudiante_);
                return;
            }
        aux = aux->getSiguiente();
        }
        cout<<"No existe ningun estudiante con este dpi"<<endl;
    }else{
       cout<< "La lista aun no tiene estudiantes"<<endl;
    }

}

void ListaEstudiantes::eliminar(string dpi_){

    NodoEstudiante *aux = this->inicio;

    if(this->inicio!=NULL){
        if(getSize()==1 && this->inicio->getEstudiante().getDpi()==dpi_){
            this->inicio=NULL;
            return;
        }
        if(this->inicio->getEstudiante().getDpi()==dpi_){
            aux->getSiguiente()->setAnterior(aux->getAnterior());
            aux->getAnterior()->setSiguiente(aux->getSiguiente());
            this->inicio=aux->getSiguiente();
            return;
        }
        aux=aux->getSiguiente();	
        while(aux !=this->inicio){
                if(aux->getEstudiante().getDpi()==dpi_){
                    aux->getSiguiente()->setAnterior(aux->getAnterior());
                    aux->getAnterior()->setSiguiente(aux->getSiguiente());
                    return;
                }
            aux = aux->getSiguiente();
            }
            cout<<"No existe ningun estudiante con este dpi"<<endl;
            return;
    }else{
       cout<< "La lista aun no tiene estudiantes"<<endl;
    }

}

bool ListaEstudiantes::carnetExist(string carnet_){

    NodoEstudiante *aux = this->inicio;
    if(this->inicio!=NULL){
    if(aux->getEstudiante().getCarnet()==carnet_){
        return true;
    }
	aux=aux->getSiguiente();	
    while(aux !=this->inicio){
            if(aux->getEstudiante().getCarnet()==carnet_){
                return true;
            }
        aux = aux->getSiguiente();
        }
        return false;
    }else{
       return false;
    }
}

void ListaEstudiantes::graficar(){
    int id=1;
    string grafica="digraph List {rankdir=LR;node [shape = note, color=blue , style=filled, fillcolor=lightgray];";
    NodoEstudiante *aux=this->inicio;
    if(this->inicio!=NULL){
        grafica=grafica+"\nNode1[label=\"Carnet:"+aux->getEstudiante().getCarnet()+"\\nNombre: "+aux->getEstudiante().getNombre()+"\\nDPI: "+aux->getEstudiante().getDpi()+"\\nCarrera: "+aux->getEstudiante().getCarrera()+"\\nCorreo: "+aux->getEstudiante().getCorreo()+"\\nPassword: "+aux->getEstudiante().getPassword()+"\\nCreditos: "+to_string(aux->getEstudiante().getCreditos())+"\\nEdad: "+to_string(aux->getEstudiante().getEdad())+"\"];\n";
        grafica=grafica+"\nNode"+to_string(id)+"->Node"+to_string(id+1);
        aux=aux->getSiguiente();
        while(aux!=this->inicio){
        id++;
        grafica=grafica+"\nNode"+to_string(id)+"[label=\"Carnet:"+aux->getEstudiante().getCarnet()+"\\nNombre: "+aux->getEstudiante().getNombre()+"\\nDPI: "+aux->getEstudiante().getDpi()+"\\nCarrera: "+aux->getEstudiante().getCarrera()+"\\nCorreo: "+aux->getEstudiante().getCorreo()+"\\nPassword: "+aux->getEstudiante().getPassword()+"\\nCreditos: "+to_string(aux->getEstudiante().getCreditos())+"\\nEdad: "+to_string(aux->getEstudiante().getEdad())+"\"];\n";
        if(aux->getSiguiente()!=this->inicio){
            grafica=grafica+"\nNode"+to_string(id)+"->Node"+to_string(id+1);
        }
        grafica=grafica+"\nNode"+to_string(id)+"->Node"+to_string(id-1);
        
        aux=aux->getSiguiente();
        }
        grafica=grafica+"\nNode1->Node"+to_string(id);
        grafica=grafica+"\nNode"+to_string(id)+"->Node1";
        grafica=grafica+"\n}";

        try{
        //Esta variable debe ser modificada para agregar su path de creacion de la Grafica
        string path = "C:\\Users\\steve\\Desktop\\";

        ofstream file;
        file.open("Graph.dot",std::ios::out);

        if(file.fail()){
            exit(1);
        }
        file<<grafica;
        file.close();
        index++;
        string command = "dot -Tpdf Graph.dot -o Estudiantes"+to_string(index)+".pdf";
        system(command.c_str());
    }catch(exception e){
        cout<<"Fallo detectado"<<endl;
    }
    }else{
        cout<<"la lista esta vacia"<<endl;
    }

}

string ListaEstudiantes::generarCodigo(){
    string texto="";
    NodoEstudiante *aux = this->inicio;
    if(this->inicio!=NULL){
    texto=texto+"\n¿element type=\"user\"?";
    texto=texto+" \n    ¿item Carnet = \""+aux->getEstudiante().getCarnet()+"\" $?";
    texto=texto+" \n    ¿item DPI = \""+aux->getEstudiante().getDpi()+"\" $?";
    texto=texto+" \n    ¿item Nombre = \""+aux->getEstudiante().getNombre()+"\" $?";
    texto=texto+" \n    ¿item Carrera = \""+aux->getEstudiante().getCarrera()+"\" $?";
    texto=texto+" \n    ¿item Password = \""+aux->getEstudiante().getPassword()+"\" $?";
    texto=texto+" \n    ¿item Creditos = \""+to_string(aux->getEstudiante().getCreditos())+"\" $?";
    texto=texto+" \n    ¿item Edad = \""+to_string(aux->getEstudiante().getEdad())+"\" $?";
    texto=texto+" \n    ¿item Correo = \""+aux->getEstudiante().getCorreo()+"\" $?";
    texto=texto+"\n¿$element?";
	aux=aux->getSiguiente();	
    while(aux !=this->inicio){
        texto=texto+"\n¿element type=\"user\"?";
         texto=texto+" \n   ¿item Carnet = \""+aux->getEstudiante().getCarnet()+"\" $?";
        texto=texto+" \n    ¿item DPI = \""+aux->getEstudiante().getDpi()+"\" $?";
        texto=texto+" \n    ¿item Nombre = \""+aux->getEstudiante().getNombre()+"\" $?";
        texto=texto+" \n    ¿item Carrera = \""+aux->getEstudiante().getCarrera()+"\" $?";
        texto=texto+" \n    ¿item Password = \""+aux->getEstudiante().getPassword()+"\" $?";
        texto=texto+" \n    ¿item Creditos = \""+to_string(aux->getEstudiante().getCreditos())+"\" $?";
        texto=texto+" \n    ¿item Edad = \""+to_string(aux->getEstudiante().getEdad())+"\" $?";
        texto=texto+" \n    ¿item Correo = \""+aux->getEstudiante().getCorreo()+"\" $?";
        texto=texto+"\n¿$element?";
        aux = aux->getSiguiente();
        }
    }

    return texto;

}

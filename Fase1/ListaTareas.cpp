#include "ListaTareas.h"
#include <iostream>
#include <fstream>
using namespace std;
int indice=0;

ListaTareas::ListaTareas(){

    this->primero=NULL;
    this->ultimo=NULL;
}

bool ListaTareas::isEmpty(){

    return this->primero==NULL;
}

int ListaTareas::getSize(){

    NodoTarea *aux = this->primero;
    int contador = 0;
	
    while(aux != NULL){
        contador++;
        aux = aux->getSiguiente();
        }
        return contador;
    }


void ListaTareas::insertar(Tarea tarea_){

    NodoTarea *newNodo = new NodoTarea(tarea_);
    NodoTarea *aux = this->primero;
    if (this->primero==NULL){
        this->primero=newNodo;
        this->ultimo=primero;
    }else{
        newNodo->setAnterior(this->ultimo);
        this->ultimo->setSiguiente(newNodo);
        this->ultimo=newNodo;
    }
}

void ListaTareas::imprimir(){
    NodoTarea *aux = this->primero;
    if(this->primero!=NULL){	
    while(aux != NULL){
        if(aux->getTarea().getNombre()!= "-1"){
        aux->getTarea().toString();
        }
        aux = aux->getSiguiente();
        }
    }else{
        cout<<"La lista de estudiantes aun no tiene elementos"<<endl;
    }
}

Tarea ListaTareas::searchTarea(string id_){

    NodoTarea *aux = this->primero;
    if(this->primero!=NULL){	
    while(aux !=NULL){
            if(aux->getTarea().getId()==stoi(id_)){
        return aux->getTarea();
        }
        aux = aux->getSiguiente();
        }
        cout<<"No existe ningun estudiante con este dpi"<<endl;
    }else{
       cout<< "La lista aun no tiene estudiantes"<<endl;
    }
}

bool ListaTareas::exist(string id_){

    NodoTarea *aux = this->primero;
    if(this->primero!=NULL){	
    while(aux !=NULL){
        if(aux->getTarea().getId()==stoi(id_)){
            if(aux->getTarea().getNombre()!="-1"){
            return true;
            }
            return false;
        }
        aux = aux->getSiguiente();
        }
        return false;
    }else{
       return false;
    }
}

void ListaTareas::modificar(string id_, Tarea tarea_){
    
    NodoTarea *aux = this->primero;
    if(aux!=NULL){	
    while(aux !=NULL){
            if(aux->getTarea().getId()==stoi(id_)){
                aux->setTarea(tarea_);
               
                return;
            }
        aux = aux->getSiguiente();
        }
        
        cout<<"No existe ningun estudiante con este dpi"<<endl;
    }else{
       cout<< "La lista aun no tiene estudiantes"<<endl;
    }
}

void ListaTareas::eliminar(string id_){
    NodoTarea *aux = this->primero;
    if(this->primero!=NULL){ 
        while(aux !=NULL){
        if(aux->getTarea().getId()==stoi(id_)){
            if(aux->getTarea().getNombre()!="-1"){
                Tarea t1 = Tarea(stoi(id_),"-1","-1","-1","-1","-1","-1","-1",0,0,0);
                aux->setTarea(t1);
                return;
            }else{
                cout<<"No se encontro una tarea con este id"<<endl;
                return;
            }
            }	
            aux = aux->getSiguiente();
            
            }
            cout<<"No existe ninguna tarea con este id"<<endl;
            return;
    }else{
       cout<< "La lista aun no tiene estudiantes"<<endl;
       return;
    }
}

void ListaTareas::graficar(){

    string grafica="digraph List {rankdir=LR;node [shape = note, color=blue , style=filled, fillcolor=lightgray];";
    NodoTarea *aux=this->primero;
    if(this->primero!=NULL){
        while(aux!=NULL){
        if(aux->getTarea().getNombre()!="-1"){
        grafica=grafica+"\nNode"+to_string(aux->getTarea().getId())+"[label=\"ID:"+to_string(aux->getTarea().getId())+"\\nNombre de Tarea: "+aux->getTarea().getNombre()+"\\nCarné: "+aux->getTarea().getCarnet()+"\\nDescripcion: "+aux->getTarea().getDescripcion()+"\\nMateria: "+aux->getTarea().getMateria()+"\\nFecha: "+aux->getTarea().getFechaS()+"\\nHora: "+aux->getTarea().getHoraS()+"\\nEstado: "+aux->getTarea().getEstado()+"\"];\n";
        }else{
            grafica=grafica+"\nNode"+to_string(aux->getTarea().getId())+"[label=\"ID:"+to_string(aux->getTarea().getId())+"\\n -1\"];\n";
        }
        if (aux->getSiguiente()!=NULL){
            grafica=grafica+"\nNode"+to_string(aux->getTarea().getId())+"->Node"+to_string(aux->getTarea().getId()+1);
        }
        if (aux->getAnterior()!=NULL){
            grafica=grafica+"\nNode"+to_string(aux->getTarea().getId())+"->Node"+to_string(aux->getTarea().getId()-1);
        }
        aux=aux->getSiguiente();
        }
        
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
        indice++;
        string command = "dot -Tpdf Graph.dot -o Tareas"+to_string(indice)+".pdf";
        system(command.c_str());
    }catch(exception e){
        cout<<"Fallo detectado"<<endl;
    }
    }else{
        cout<<"la lista esta vacia"<<endl;
    }

}

string ListaTareas::generarCodigo(){
    string texto="";

    NodoTarea *aux = this->primero;
    if(this->primero!=NULL){	
    while(aux != NULL){
        if(aux->getTarea().getNombre()!= "-1"){
        texto=texto+"\n¿element type=\"task\"?";
        texto=texto+" \n    ¿item Carnet = \""+aux->getTarea().getCarnet()+"\" $?";
        texto=texto+" \n    ¿item Nombre = \""+aux->getTarea().getNombre()+"\" $?";
        texto=texto+" \n    ¿item Descripcion = \""+aux->getTarea().getDescripcion()+"\" $?";
        texto=texto+" \n    ¿item Materia = \""+aux->getTarea().getMateria()+"\" $?";
        texto=texto+" \n    ¿item Fecha = \""+aux->getTarea().getFechaS()+"\" $?";
        texto=texto+" \n    ¿item Hora = \""+aux->getTarea().getHoraS()+"\" $?";
        texto=texto+" \n    ¿item Estado = \""+aux->getTarea().getEstado()+"\" $?";
        texto=texto+"\n¿$element?";
        }
        aux = aux->getSiguiente();
        }
        return texto;
    }else{
        cout<<"La lista de estudiantes aun no tiene elementos"<<endl;
    }

    return texto;


}

#include "ListaTareas.h"
#include <iostream>
using namespace std;

ListaTareas::ListaTareas(){

    this->primero=NULL;
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


void ListaTareas::insertar(Tarea tarea_, string id_){

    NodoTarea *newNodo = new NodoTarea(tarea_);
    if (isEmpty()){
        this->primero=newNodo;
    }else{
        NodoTarea *aux = this->primero;
        while(aux->getSiguiente()!=NULL){
            aux=aux->getSiguiente();
        }
        newNodo->setAnterior(aux);
        aux->setSiguiente(newNodo);
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
    if(this->primero!=NULL){	
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

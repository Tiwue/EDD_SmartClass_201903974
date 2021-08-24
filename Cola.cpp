#include "Cola.h"
#include <iostream>
#include <fstream>
using namespace std;
int idDocumento=0;
Cola::Cola(){
    this->primero=NULL;
}

bool Cola::isEmpty(){
    return this->primero==NULL;
}

int Cola::getSize(){
    NodoCola *aux = this->primero;
    int contador = 0;
    while(aux !=NULL){
        contador++;
        aux = aux->getSiguiente();
    }
    return contador;
}

void Cola::recorrer(){
    NodoCola *aux = this->primero;
    if(this->primero!=NULL){
    while(aux !=NULL){
        aux->getError().toString();
        aux = aux->getSiguiente();
        }
    }else{
        cout<<"La cola aun no tiene elementos"<<endl;
    }
}

void Cola::encolar(Error error_){
    NodoCola *newNodo = new NodoCola(error_);
    if (isEmpty()){
        this->primero=newNodo;
    }else{
        NodoCola *aux = this->primero;
        while(this->primero->getSiguiente() !=NULL){
            this->primero=this->primero->getSiguiente();
        }
        this->primero->setSiguiente(newNodo);
        this->primero=aux;
    }

}

void Cola::desencolar(){

    if (isEmpty()){
        cout<<"La cola esta vacía, no hay elementos para desencolar"<<endl;
    }else{
        cout<<"Se ha desencolado el siguiente elemento:"<<endl;
        this->primero->getError().toString();
        this->primero=this->primero->getSiguiente();
    }
}

void Cola::graficar(){
    int ultimo=0;
    string grafica="digraph List {rankdir=LR;node [shape = box3d, color=blue , style=filled, fillcolor=lightgray];\nentrada[shape=larrow ]\nsalida[shape=larrow]\nsalida->Node"+to_string(this->primero->getError().getId());
    NodoCola *aux = this->primero;
    if(this->primero!=NULL){
        while(aux!=NULL){
        ultimo=aux->getError().getId();
        grafica=grafica+"\nNode"+to_string(aux->getError().getId())+"[label=\"ID:"+to_string(aux->getError().getId())+"\\nTipo: "+aux->getError().getTipo()+"\\nDescripcion: "+aux->getError().getDescripcion()+"\\nIdentificador: "+aux->getError().getDpi()+"\"];\n";
        
        if(aux->getSiguiente()!=NULL){
            grafica=grafica+"\nNode"+to_string(aux->getError().getId())+"->Node"+to_string(aux->getError().getId()+1);
            
        }
        aux=aux->getSiguiente();
        }
        grafica=grafica+"\nNode"+to_string(ultimo)+"->entrada[arrowhead=none]";
        
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
        idDocumento++;
        string command = "dot -Tpdf Graph.dot -o Errores"+to_string(idDocumento)+".pdf";
        system(command.c_str());
    }catch(exception e){
        cout<<"Fallo detectado"<<endl;
    }
    }else{
        cout<<"la cola esta vacia"<<endl;
    }

}


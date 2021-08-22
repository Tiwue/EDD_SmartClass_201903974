#include "Cola.h"
#include <iostream>
using namespace std;

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

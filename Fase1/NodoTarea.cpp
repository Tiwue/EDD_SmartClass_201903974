#include "NodoTarea.h"

NodoTarea::NodoTarea(){
    this->tarea=Tarea();
    this->siguiente=NULL;
    this->anterior=NULL;
}

NodoTarea::NodoTarea(Tarea tarea_){

    this->tarea = tarea_;
    this->siguiente=NULL;
    this->anterior=NULL;

}

NodoTarea::NodoTarea(Tarea tarea_, NodoTarea *siguiente_, NodoTarea *anterior_){
    this->tarea=tarea_;
    this->siguiente=siguiente;
    this->anterior=anterior;

}

Tarea NodoTarea::getTarea(){
    return this->tarea;
}

NodoTarea *NodoTarea::getSiguiente(){
    return this->siguiente;
}

NodoTarea *NodoTarea::getAnterior(){
    return this->anterior;
}
void NodoTarea::setTarea(Tarea tarea_){

    this->tarea=tarea_;

}

void NodoTarea::setSiguiente(NodoTarea *siguiente_){
    this->siguiente = siguiente_;
}

void NodoTarea::setAnterior(NodoTarea *anterior_){
    this->anterior = anterior_;
}
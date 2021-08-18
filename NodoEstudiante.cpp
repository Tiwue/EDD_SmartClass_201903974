#include "NodoEstudiante.h"

NodoEstudiante::NodoEstudiante(){
    this->estudiante=Estudiante();
    this->siguiente=NULL;
    this->anterior=NULL;
}

NodoEstudiante::NodoEstudiante(Estudiante estudiante_){

    this->estudiante = estudiante_;
    this->siguiente=NULL;
    this->anterior=NULL;

}

NodoEstudiante::NodoEstudiante(Estudiante estudiante_, NodoEstudiante *siguiente_, NodoEstudiante *anterior_){
    this->estudiante=estudiante_;
    this->siguiente=siguiente;
    this->anterior=anterior;

}

Estudiante NodoEstudiante::getEstudiante(){
    return this->estudiante;
}

NodoEstudiante *NodoEstudiante::getSiguiente(){
    return this->siguiente;
}

NodoEstudiante *NodoEstudiante::getAnterior(){
    return this->anterior;
}
void NodoEstudiante::setEstudiante(Estudiante estudiante_){

    this->estudiante=estudiante_;

}

void NodoEstudiante::setSiguiente(NodoEstudiante *siguiente_){
    this->siguiente = siguiente_;
}

void NodoEstudiante::setAnterior(NodoEstudiante *anterior_){
    this->anterior = anterior_;
}
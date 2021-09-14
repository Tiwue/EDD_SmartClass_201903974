#include "NodoCola.h"

NodoCola::NodoCola(){
    this->error=Error();
    this->siguiente=NULL;
}

NodoCola::NodoCola(Error error_){
    this->error = error_;
    this->siguiente=NULL;
}

NodoCola::NodoCola(Error error_, NodoCola *siguiente_){
    this->error=error_;
    this->siguiente=siguiente_;
}

Error NodoCola::getError(){
    return this->error;
}

NodoCola *NodoCola::getSiguiente(){
    return this->siguiente;
}

void NodoCola::setError(Error error_){
    this->error=error_;

}

void NodoCola::setSiguiente(NodoCola *siguiente_){
    this->siguiente = siguiente_;
}
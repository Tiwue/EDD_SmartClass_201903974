#include <iostream>
#include <stdlib.h>
#include <string>
#include "Error.h""

Error::Error(){

     id = 0;
     tipo= "";
     descripcion="";

};

Error::Error(int id_, string tipo_, string descripcion_){

     id = id_;
     tipo= tipo_;
     descripcion = descripcion_;     
};

void Error::toString(){
     
    cout<< "\nID: "<<id<<"\nTipo: "<<tipo<<"\nDescripcion: "<<descripcion<<endl;
};

void Error::setId(int id_){

     this->id=id_;
}

void Error::setTipo(string tipo_){

     this->tipo=tipo_;
}
void Error::setDescripcion(string descripcion_){

     this->descripcion=descripcion_;
}

int Error::getId(){
     return this->id;
}

string Error::getTipo(){
     return this->tipo;
}

string Error::getDescripcion(){
     return this->descripcion;
}

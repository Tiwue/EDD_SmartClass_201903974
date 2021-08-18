#include <iostream>
#include <stdlib.h>
#include <string>
#include "Error.h""

Error::Error(){

     id = 0;
     dpi="";
     tipo= "";
     descripcion="";

};

Error::Error(int id_, string tipo_, string descripcion_, string dpi_){

     id = id_;
     tipo= tipo_;
     descripcion = descripcion_;   
     dpi= dpi_;  
};

void Error::toString(){
    cout<<"\nID: "<<id<<"\nTipo: "<<tipo<<"\nDPI: "<<dpi<<"\nDescripcion: "<<descripcion<<endl;
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

void Error::setDpi(string dpi_){
     this->dpi=dpi_;
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

string Error::getDpi(){
     return this->dpi;
}
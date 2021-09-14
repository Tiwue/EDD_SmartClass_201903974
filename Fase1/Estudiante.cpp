#include <iostream>
#include <stdlib.h>
#include <string>
#include "Estudiante.h"

Estudiante::Estudiante(){

     nombre = "";
     carnet= "";
     dpi = "";
     edad = 0;
     carrera = "";
     correo = "";
     password = "";
     creditos = 0;

};

Estudiante::Estudiante(string _nombre, int _edad, string carnet_,string dpi_, int creditos_, string carrera_, string correo_, string password_){

     nombre = _nombre;
     carnet= carnet_;
     dpi = dpi_;
     edad = _edad;
     carrera = carrera_;
     correo = correo_;
     password = password_;
     creditos = creditos_;

};

void Estudiante::toString(){
     
    cout<< "\nNombre: "<<nombre<<"\nCarnet: "<<carnet<<"\nDPI: "<<dpi<<"\nCarrera: "<<carrera<<"\nPassword: "<<password<<"\nCreditos: "<<creditos<<"\nEdad: "<<edad<<"\nCorreo: "<< correo<<endl;
};

void Estudiante::setNombre(string nombre_){

     this->nombre=nombre_;
}

void Estudiante::setCarnet(string carnet_){

     this->carnet=carnet_;
}
void Estudiante::setDpi(string dpi_){

     this->dpi=dpi_;
}
void Estudiante::setEdad(int edad_){

     this->edad=edad_;
}
void Estudiante::setCarrera(string carrera_){

     this->carrera=carrera_;
}
void Estudiante::setCorreo(string correo_){

     this->correo=correo_;
}
void Estudiante::setPassword(string password_){

     this->password=password_;
}
void Estudiante::setCreditos(int creditos_){

     this->creditos=creditos_;
}

string Estudiante::getNombre(){
     return this->nombre;
}

string Estudiante::getCarnet(){
     return this->carnet;
}

string Estudiante::getDpi(){
     return this->dpi;
}
int Estudiante::getEdad(){
     return this->edad;
}

string Estudiante::getCarrera(){
     return this->carrera;
}

string Estudiante::getCorreo(){
     return this->correo;
}

string Estudiante::getPassword(){
     return this->password;
}

int Estudiante::getCreditos(){
     return this->creditos;
}
#include <iostream>
#include <stdlib.h>
#include <string>
#include "Tarea.h"

Tarea::Tarea(){

    id = 0;
    nombre = "";
    carnet= "";
    descripcion = "";
    materia = "";
    horaS = "";
    fechaS = "";
    mes = 0;
    dia = 0;
    hora= 0;
};

Tarea::Tarea(int id_, string nombre_,string carnet_, string descripcion_, string materia_, string horaS_, string fechaS_, string estado_, int mes_, int dia_, int hora_){
    id = id_;
    nombre = nombre_;
    carnet= carnet_;
    descripcion = descripcion_;
    materia = materia_;
    horaS = horaS_;
    fechaS = fechaS_;
    estado = estado_;
    mes = mes_;
    dia=dia_;
    hora=hora_;
};

void Tarea::toString(){
     
    cout<<"\nID: "<<id<< "\nNombre: "<<nombre<<"\nCarnet: "<<carnet<<"\nDescripcion: "<<descripcion<<"\nMateria: "<<materia<<"\nHora: "<<horaS<<"\nFecha: "<<fechaS<<"\nEstado: "<<estado<<endl;
};

void Tarea::setId(int id_){
    this->id=id_;
}

void Tarea::setNombre(string nombre_){

     this->nombre=nombre_;
}

void Tarea::setCarnet(string carnet_){

     this->carnet=carnet_;
}
void Tarea::setDescripcion(string descripcion_){

     this->descripcion=descripcion_;
}
void Tarea::setMateria(string materia_){

     this->materia=materia_;
}
void Tarea::setHoraS(string horaS_){

     this->horaS=horaS_;
}

void Tarea::setFechaS(string fechaS_){

     this->fechaS=fechaS_;
}
void Tarea::setEstado(string estado_){

     this->estado=estado_;
}
void Tarea::setMes(int mes_){

     this->mes=mes_;
}

void Tarea::setDia(int dia_){

     this->dia=dia_;
}

void Tarea::setHora(int hora_){

     this->hora=hora_;
}

int Tarea::getId(){
     return this->id;
}
string Tarea::getNombre(){
     return this->nombre;
}

string Tarea::getCarnet(){
     return this->carnet;
}

string Tarea::getDescripcion(){
     return this->descripcion;
}
string Tarea::getMateria(){
     return this->materia;
}

string Tarea::getHoraS(){
     return this->horaS;
}

string Tarea::getFechaS(){
     return this->fechaS;
}

string Tarea::getEstado(){
     return this->estado;
}

int Tarea::getMes(){
     return this->mes;
}

int Tarea::getDia(){
     return this->dia;
}
int Tarea::getHora(){
     return this->hora;
}
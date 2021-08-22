#include "ListaEstudiantes.h"
#include <iostream>
using namespace std;

ListaEstudiantes::ListaEstudiantes(){

    this->inicio=NULL;
}

bool ListaEstudiantes::isEmpty(){

    return this->inicio==NULL;
}

int ListaEstudiantes::getSize(){

    NodoEstudiante *aux = this->inicio;
    int contador = 0;

    if(this->inicio!=NULL){
    contador++;
	aux=aux->getSiguiente();	
    while(aux !=this->inicio){
        contador++;
        aux = aux->getSiguiente();
        }
        return contador;
    }else{
        cout<<"La lista de estudiantes aun no tiene elementos"<<endl;
        return 0;
    }
}

void ListaEstudiantes::insertar(Estudiante estudiante_){

    NodoEstudiante *newNodo = new NodoEstudiante(estudiante_);
    if (isEmpty()){
        this->inicio=newNodo;
        this->inicio->setSiguiente(newNodo);
        this->inicio->setAnterior(newNodo);
    }else{
        NodoEstudiante *aux = this->inicio;
        while(aux->getSiguiente()!=this->inicio){
            aux=aux->getSiguiente();
        }
        aux->setSiguiente(newNodo);
        newNodo->setAnterior(aux);
        newNodo->setSiguiente(this->inicio);
        this->inicio->setAnterior(newNodo);
    }

}

void ListaEstudiantes::imprimir(){
    NodoEstudiante *aux = this->inicio;
    if(this->inicio!=NULL){
    aux->getEstudiante().toString();
	aux=aux->getSiguiente();	
    while(aux !=this->inicio){
        aux->getEstudiante().toString();
        aux = aux->getSiguiente();
        }
    }else{
        cout<<"La lista de estudiantes aun no tiene elementos"<<endl;
    }
}

Estudiante ListaEstudiantes::searchEstudiante(string dpi_){

    NodoEstudiante *aux = this->inicio;
    if(this->inicio!=NULL){
    if(aux->getEstudiante().getDpi()==dpi_){
        return aux->getEstudiante();
    }
	aux=aux->getSiguiente();	
    while(aux !=this->inicio){
            if(aux->getEstudiante().getDpi()==dpi_){
                return aux->getEstudiante();
            }
        aux = aux->getSiguiente();
        }
        cout<<"No existe ningun estudiante con este dpi"<<endl;
        
    }else{
       cout<< "La lista aun no tiene estudiantes"<<endl;
       
    }
}

bool ListaEstudiantes::exist(string dpi_){

    NodoEstudiante *aux = this->inicio;
    if(this->inicio!=NULL){
    if(aux->getEstudiante().getDpi()==dpi_){
        return true;
    }
	aux=aux->getSiguiente();	
    while(aux !=this->inicio){
            if(aux->getEstudiante().getDpi()==dpi_){
                return true;
            }
        aux = aux->getSiguiente();
        }
        return false;
    }else{
       return false;
    }
}

void ListaEstudiantes::modificar(string dpi_, Estudiante estudiante_){
    
    NodoEstudiante *aux = this->inicio;
    if(this->inicio!=NULL){
    if(aux->getEstudiante().getDpi()==dpi_){
        aux->setEstudiante(estudiante_);
        return;
    }
	aux=aux->getSiguiente();	
    while(aux !=this->inicio){
            if(aux->getEstudiante().getDpi()==dpi_){
                aux->setEstudiante(estudiante_);
                return;
            }
        aux = aux->getSiguiente();
        }
        cout<<"No existe ningun estudiante con este dpi"<<endl;
    }else{
       cout<< "La lista aun no tiene estudiantes"<<endl;
    }

}

void ListaEstudiantes::eliminar(string dpi_){

    NodoEstudiante *aux = this->inicio;

    if(this->inicio!=NULL){
        if(getSize()==1 && this->inicio->getEstudiante().getDpi()==dpi_){
            this->inicio=NULL;
            return;
        }
        if(this->inicio->getEstudiante().getDpi()==dpi_){
            aux->getSiguiente()->setAnterior(aux->getAnterior());
            aux->getAnterior()->setSiguiente(aux->getSiguiente());
            this->inicio=aux->getSiguiente();
            return;
        }
        aux=aux->getSiguiente();	
        while(aux !=this->inicio){
                if(aux->getEstudiante().getDpi()==dpi_){
                    aux->getSiguiente()->setAnterior(aux->getAnterior());
                    aux->getAnterior()->setSiguiente(aux->getSiguiente());
                    return;
                }
            aux = aux->getSiguiente();
            }
            cout<<"No existe ningun estudiante con este dpi"<<endl;
            return;
    }else{
       cout<< "La lista aun no tiene estudiantes"<<endl;
    }

}

bool ListaEstudiantes::carnetExist(string carnet_){

    NodoEstudiante *aux = this->inicio;
    if(this->inicio!=NULL){
    if(aux->getEstudiante().getCarnet()==carnet_){
        return true;
    }
	aux=aux->getSiguiente();	
    while(aux !=this->inicio){
            if(aux->getEstudiante().getCarnet()==carnet_){
                return true;
            }
        aux = aux->getSiguiente();
        }
        return false;
    }else{
       return false;
    }
}


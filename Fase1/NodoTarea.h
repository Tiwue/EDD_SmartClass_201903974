#include <iostream>
#include <stdlib.h>
#include <string>
using namespace std;
#include "Tarea.cpp"

class NodoTarea{
private:
    Tarea tarea;
    NodoTarea *siguiente;
    NodoTarea *anterior;

    public:
        NodoTarea(Tarea tarea_);
        NodoTarea();
        NodoTarea(Tarea estudiante_, NodoTarea *siguiente_, NodoTarea *anterior_);
    
    Tarea getTarea();
    NodoTarea *getSiguiente();
    NodoTarea *getAnterior();


    void setTarea(Tarea tarea_);
    void setSiguiente(NodoTarea *nodo_);
    void setAnterior(NodoTarea *nodo_);
};
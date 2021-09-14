#include <iostream>
#include <stdlib.h>
#include <string>
using namespace std;
#include "Estudiante.cpp"
class NodoEstudiante{
private:
    Estudiante estudiante;
    NodoEstudiante *siguiente;
    NodoEstudiante *anterior;

    public:
        NodoEstudiante(Estudiante estudiante_);
        NodoEstudiante();
        NodoEstudiante(Estudiante estudiante_, NodoEstudiante *siguiente_, NodoEstudiante *anterior_);
    
    Estudiante getEstudiante();
    NodoEstudiante *getSiguiente();
    NodoEstudiante *getAnterior();


    void setEstudiante(Estudiante estudiante_);
    void setSiguiente(NodoEstudiante *nodo_);
    void setAnterior(NodoEstudiante *nodo_);
};
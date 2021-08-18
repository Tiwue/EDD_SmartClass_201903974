#include <iostream>
#include <stdlib.h>
#include <string>
using namespace std;
#include "Error.cpp"
class NodoCola{
private:
    Error error;
    NodoCola *siguiente;
    public:
        NodoCola(Error error_);
        NodoCola();
        NodoCola(Error error_, NodoCola *siguiente_);
    
    Error getError();
    NodoCola *getSiguiente();

    void setError(Error error_);
    void setSiguiente(NodoCola *siguiente_);

};
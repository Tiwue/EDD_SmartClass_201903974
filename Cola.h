#include "NodoCola.cpp"

class Cola{
    private:
    NodoCola *primero;

    public:
    Cola();
    bool isEmpty();
    int getSize();
    void encolar(Error error_);
    void desencolar();
    void recorrer();
    void graficar();
};
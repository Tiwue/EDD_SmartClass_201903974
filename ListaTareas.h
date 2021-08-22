#include "NodoTarea.cpp"

class ListaTareas{
    private:
    NodoTarea *primero;
    

    public:
    ListaTareas();
    bool isEmpty();
    Tarea searchTarea(string id_);
    bool exist(string dpi_);
    int getSize();
    void append(Tarea tarea_, string id_);
    void insertar(Tarea tarea_, string id_);
    void eliminar(string id_);
    void imprimir();
    void modificar(string id_, Tarea modificado_);

};
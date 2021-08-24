#include "NodoEstudiante.cpp"

class ListaEstudiantes{
    private:
    NodoEstudiante *inicio;
    

    public:
    ListaEstudiantes();
    bool isEmpty();
    Estudiante searchEstudiante(string dpi_);
    bool exist(string dpi_);
    int getSize();
    void insertar(Estudiante estudiante_);
    void eliminar(string dpi_);
    void modificar(string dpi_);
    void imprimir();
    void modificar(string dpi_, Estudiante modificado_);
    bool carnetExist(string carnet_);
    void graficar();
    string generarCodigo();
};
#include <iostream>
#include <stdlib.h>
#include <string>
using namespace std;

class Error{
public:
    int id;
    string tipo;
    string descripcion;

    Error();
    Error(int id_,string tipo_, string descripcion_ );
    
    void setId(int id_);
    void setTipo(string tipo_);
    void setDescripcion(string descripcion_);
    void toString();

    int getId();
    string getTipo();
    string getDescripcion();
    
};
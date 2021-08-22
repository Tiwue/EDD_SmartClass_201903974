#include <iostream>
#include <stdlib.h>
#include <string>
using namespace std;

class Tarea{
public:
    int id;
    string nombre;
    string carnet;
    string descripcion;
    string materia;
    string horaS;
    string fechaS;
    string estado;
    int mes;
    int dia;
    int hora;


    Tarea();
    Tarea(int id_, string nombre_,string carnet_, string descripcion_, string materia_, string horaS_, string fechaS_, string estado_, int mes_, int dia_, int hora_);
    void toString();
    void setId(int id_);
    void setNombre(string nombre_);
    void setCarnet(string carnet_);
    void setDescripcion(string descripcion_);
    void setMateria(string materia_);
    void setHoraS(string horaS_);
    void setFechaS(string fechaS_);
    void setEstado(string estado_);
    void setMes(int mes_);
    void setDia(int dia_);
    void setHora(int hora_);

    int getId();
    string getNombre();
    string getCarnet();
    string getDescripcion();
    string getMateria();
    string getHoraS();
    string getFechaS();
    string getEstado();
    int getMes();
    int getDia();
    int getHora();
};
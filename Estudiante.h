#include <iostream>
#include <stdlib.h>
#include <string>
using namespace std;

class Estudiante{
public:
    string nombre;
    string carnet;
    string dpi;
    int edad;
    string carrera;
    string correo;
    string password;
    int creditos;


    Estudiante();
    Estudiante(string _nombre, int _edad,string carnet_, string dpi_, int creditos_, string carrera_, string correo_, string password_);
    void toString();
    void setNombre(string nombre_);
    void setCarnet(string carnet_);
    void setDpi(string dpi_);
    void setEdad(int edad_);
    void setCarrera(string carrera_);
    void setCorreo(string correo_);
    void setPassword(string password_);
    void setCreditos(int creditos_);

    string getNombre();
    string getCarnet();
    string getDpi();
    int getEdad();
    string getCarrera();
    string getCorreo();
    string getPassword();
    int getCreditos();
};

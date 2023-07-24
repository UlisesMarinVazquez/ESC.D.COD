


#include<iostream>
#include<vector>
using namespace std;

class Persona{
 private:
 int edad;
 string nombre;
 string apellidoPaterno;
 string apellidoMaterno;
 public:
 Persona(int edad , string nombre , string apellidoPaterno , string apellidoMaterno){
 this->edad = edad;
 this->nombre = nombre;
 this->apellidoPaterno = apellidoPaterno;
 this->apellidoMaterno = apellidoMaterno;
 }
 void setEdad(int edad){
 this->edad = edad;
 }
 void setNombre(string nombre){
 this->nombre = nombre;
 }
 void setApellidoPaterno(string apellidoPaterno){
 this->apellidoPaterno = apellidoPaterno;
 }
 void setApellidoMaterno(string apellidoMaterno){
 this->apellidoMaterno = apellidoMaterno;
 }
 int getEdad(){
 return this->edad;
 }
 string getNombre(){
 return this->nombre;
 }
 string getApellidoPaterno(){
 return this->apellidoPaterno;
 }
 string getApellidoMaterno(){
 return this->apellidoMaterno;
 }
};
class Empleado : public Persona{
 private:
 int horasLaborales;
 double sueldo;
 public:
 Empleado(int edad, string nombre , string apellidoPaterno , string apellidoMaterno , int horasLaborales , double sueldo) : Persona(edad , nombre , apellidoPaterno , apellidoMaterno){
 this->horasLaborales = horasLaborales;
 this->sueldo = sueldo; 
 }
 void setHorasLaborales(int horasLaborales){
 this->horasLaborales = horasLaborales; 
 } 
 void setSueldo(double sueldo){
 this->sueldo = sueldo; 
 }
 int getHorasLaborales(){
 return this->horasLaborales;
 }
 double getSueldo(){
 return this->sueldo;
 }
 void metodo(){
 cout << "El nombre del empleado es: " << getNombre() << endl;
 cout << "El apellido paterno es: " << getApellidoPaterno() << endl;
 cout << "El apellido materno es: " << getApellidoMaterno() << endl;
 cout << "La edad es: " << getEdad() << endl;
 cout << "La horas laborales son: " << getHorasLaborales() << endl;
 cout << "El sueldo es: " << getSueldo() << endl;
 }
};
class Estudiante : public Persona{
 private:
 string grupo;
 double notaFinal;
 public:
 Estudiante(string nombre , int edad , string apellidoPaterno , string apellidoMaterno , string grupo , double notaFinal) : Persona(edad , nombre ,  apellidoPaterno , apellidoMaterno){
 this->grupo = grupo;
 this->notaFinal = notaFinal;
 }
 void setGrupo(string grupo){
 this->grupo = grupo;
 }
 void setNotaFinal(double ){
 this->notaFinal = notaFinal;
 }
 string getGrupo(){
 return this->grupo;
 }
 double getNotaFinal(){
 return this->notaFinal;
 }
 void metodo(){
 cout << "El nombre del estudiante es: " << getNombre() << endl;
 cout << "El apellido paterno es: " << getApellidoPaterno() << endl;
 cout << "EL apellido materno es: " << getApellidoMaterno() << endl;
 cout << "La edad del estudiante es: " << getEdad() << endl;
 cout << "EL grupo es: " << getGrupo() << endl;
 cout << "La nota final del alumno es: " << getNotaFinal() << endl;
 }
};
class Universitario : public Estudiante{
 private:
 string carrera;
 public:
 Universitario(string nombre , int edad , string apellidoPaterno , string apellidoMaterno , string grupo , double notaFinal , string carrera) : Estudiante(nombre , edad , apellidoPaterno , apellidoMaterno , grupo , notaFinal){
 this->carrera = carrera;
 }
 void setCarrera(string carrera){
 this->carrera = carrera;
 }
 string getCarrera(){
 return this->carrera;
 }
 void metodo(){
 cout << "La carrera que decea estudiar el universitario es: " << getCarrera() << endl;
 cout << "El nombre del estudiante es: " << getNombre() << endl;
 cout << "El apellido paterno es: " << getApellidoPaterno() << endl;
 cout << "EL apellido materno es: " << getApellidoMaterno() << endl;
 cout << "La edad del estudiante es: " << getEdad() << endl;
 cout << "EL grupo es: " << getGrupo() << endl;
 cout << "La nota final del alumno es: " << getNotaFinal() << endl;
 }
};
string pedirNombre(){
 string nombre;
 cout << "Dame el nombre: ";
 cin >> nombre;
 return nombre;
}
string pedirApellidoPaterno(){
 string apellidoPaterno;
 cout << "Dame el apellido paterno: ";
 cin >> apellidoPaterno;
 return apellidoPaterno;
}
string pedirApellidoMaterno(){
 string apellidoMaterno;
 cout << "Dame el apellido materno: ";
 cin >> apellidoMaterno;
 return apellidoMaterno;
}
int pedirEdad(){
 int edad;
 cout << "Dame la edad: ";
 cin >> edad;
 return edad;
}
int pedirHorasLaborales(){
 int horasLaborales;
 cout << "Dame las horas laborales: ";
 cin >> horasLaborales;
 return horasLaborales;
}
double pedirSueldo(){
 double sueldo;
 cout << "Dame el sueldo: ";
 cin >> sueldo;
 return sueldo;
}
string pedirGrupo(){
 string grupo;
 cout << "Dame el grupo: ";
 cin >> grupo;
 return grupo;
}
double pedirNotaFinal(){
 double notaFinal;
 cout << "Dame la nota final: ";
 cin >> notaFinal;
 return notaFinal;
}
string pedirCarrera(){
 string carrera;
 cout << "Dame la carrera: ";
 cin >> carrera;
 return carrera;
}
vector<Empleado> listaEmpleados;
vector<Estudiante> listaEstudiante;
vector<Universitario> listaUniversitario;
void imprimirListaEmpleados(vector<Empleado> listaEmpleados){
 for(int i = 0; i < listaEmpleados.size(); i++){
 listaEmpleados.at(i).metodo();
 } 
 cout << endl;
}
void imprimirListaEstudiante(vector<Estudiante> listaEstudiantes){
 for(int i = 0; i < listaEstudiantes.size(); i++){
 listaEstudiantes.at(i).metodo();
 }
 cout << endl;
}
void imprimirListaUniversitario(vector<Universitario> listaUniversitarios){
 for(int i = 0; i < listaUniversitarios.size(); i++){
 listaUniversitarios.at(i).metodo();
 }
 cout << endl;
}
int main(){
 int opcion;
 bool continuarConElMenu = false;
 string nombre;
 string apellidoPaterno;
 string apellidoMaterno;
 string grupo;
 string carrera;
 double notaFinal;
 int edad;
 int horasLaborales;
 double sueldo;
 do{
 do{
 cout << "-------------------- MENU --------------------" << endl;
 cout << "1.Agregar Empleado" << endl;
 cout << "2.Agregar Estudiante" << endl;
 cout << "3.Agregar universitario" << endl;
 cout << "4.Mostrar lista de empleados" << endl;
 cout << "5.Mostrar lista de estudiantes" << endl;
 cout << "6.Mostrar lista de universitarios" << endl;
 cout << "7.Salir" << endl;
 cout << "Seleccion una opcion: ";
 cin >> opcion;
 cout << endl;
 }while(opcion < 1 || opcion > 7);
 switch(opcion){
 case 1:
 nombre = pedirNombre();
 apellidoPaterno = pedirApellidoPaterno();
 apellidoMaterno = pedirApellidoMaterno();
 edad = pedirEdad();
 horasLaborales = pedirHorasLaborales();
 sueldo = pedirSueldo();
 listaEmpleados.push_back(Empleado(edad , nombre , apellidoPaterno , apellidoMaterno , horasLaborales , sueldo));
 break;
 case 2:
 nombre = pedirNombre();
 apellidoPaterno = pedirApellidoPaterno();
 apellidoMaterno = pedirApellidoMaterno();
 edad = pedirEdad();
 grupo = pedirGrupo();
 notaFinal = pedirNotaFinal();
 listaEstudiante.push_back(Estudiante(nombre , edad , apellidoPaterno , apellidoMaterno , grupo , notaFinal));
 break;
 case 3:
 nombre = pedirNombre();
 apellidoPaterno = pedirApellidoPaterno();
 apellidoMaterno = pedirApellidoMaterno();
 edad = pedirEdad();
 grupo = pedirGrupo();
 notaFinal = pedirNotaFinal();
 carrera = pedirCarrera();
 listaUniversitario.push_back(Universitario(nombre , edad , apellidoPaterno , apellidoMaterno , grupo , notaFinal , carrera));
 break;
 case 4:
 imprimirListaEmpleados(listaEmpleados);
 break;
 case 5:
 imprimirListaEstudiante(listaEstudiante);
 break;
 case 6:
 imprimirListaUniversitario(listaUniversitario);
 break;
 case 7:
 continuarConElMenu = true;
 break;
 }
 }while(continuarConElMenu == false);
 return 0;
}

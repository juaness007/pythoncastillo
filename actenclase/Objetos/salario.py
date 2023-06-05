#Escriba una clase Empleado que tenga como propiedades
#nombre, cargo, salario
#escriba metodos contructores, setters y getters
#*Escriba un método que permita calcular cuanto gana el empleado en una hora
#*Un método para saber cuanto recibe de incremento si el salario sube con el IPC. Si gana el mínimo se le aumenta el ipc + 3%
#*Un método que reciba una cantidad de horas extras y calcule el salario incrementando las extras. No puede hacer mas de dos horas diarias y trabaja de luenes a viernes. Valide

#Debe tener dos variables de clase. Suma, para sumar todos los salarios y contador para promediarlos
#*Metodo para visualizar la suma de los salarios
#*Método para calcularel promedio de los salarios

class Empleado:
    def __init__(self,nombre,cargo,salario):
        self.__nombre=nombre
        self.__cargo=cargo
        self.__salario=salario

    def getNombre(self):
        return self.__nombre
    
    def getCargo(self):
        return self.__cargo        
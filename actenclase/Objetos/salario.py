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
    
    def getSalario(self):
        return self.__salario

    def setNom(self,nombre):
        self.__nombre=nombre  

    def setCargo(self,cargo):
        self.__cargo=cargo    

    def setSalario(self,salario):
        self.__salario=salario
    def horaLab(self):
        return round(self.__salario/240)

e1=Empleado('Juanes','Ingeniero',1300000)        
e2=Empleado('Jaimito','Cartero',5500000)
print(e1.getNombre())
print(e1.getCargo())
print(e1.getSalario())
print(e1.horaLab())
print(e2.getNombre())
print(e2.getCargo())
print(e2.getSalario())
print(e2.horaLab())
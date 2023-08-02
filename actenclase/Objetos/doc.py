class Persona:
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
        
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre
    
    def getDocumento(self):
        return self.__documento
    def setDocumento(self,documento):
        self.__documento=documento        
        
    def mostrarDatos(self):
        print('los datos de la persona son: ')
        return self.__nombre, self.__documento    
    
    listaCursos=[]
    
    def añadirCurso(self):
        curso=[]
        curso=[input('introduzca cursos: ')]
        return 
    
    def buscarCurso():
        for curso in curso:
            print('El nombre del curso es :', curso.nombrecurso)
        
        
        
        
p=Persona('Ana',123)
print(p.getNombre())
q=Persona('Pedro',321)
print(q.getNombre())
print(p.getDocumento())
print(q.getDocumento())
print(q.mostrarDatos())
print(p.añadirCurso())
print(p.buscarCurso())


        
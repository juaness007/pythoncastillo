class Persona:
    Cursos=[]
    def _init_(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
        self.__curso=[]
    def getNombre(self):
        return self.__nombre
    def getDoc(self):
        return self.__documento
    def setNom(self,nombre):
        self.__nombre=nombre
    def setDoc(self,documento):
        self.__documento=documento
    def getCurso(self):
        return self.__curso
    def setCurso(self,curso):
        self.__curso.append(curso)
        for a in self.__curso:
            if a not in Persona.Cursos:
                Persona.Cursos.append(a)
p=Persona('Diego',1024501189)
print(p.getNombre())
print(p.getDoc())
print(p.getCurso())
p.setCurso('python')
p.setCurso('c++')
p.setCurso('java')
print(p.getCurso())
pu=Persona('Juanes', 2328852014)
print(pu.getNombre())
print(pu.getDoc()) 
pu.setCurso('python')
pu.setCurso('c++')
pu.setCurso('php')
print(pu.getCurso())
pd=Persona('Jairo', 1230930927218)
pd.setCurso('python')
pd.setCurso('c++')
pd.setCurso('php')
pd.setCurso('java')
pd.setCurso('js')
print(pd.getNombre())
print(pd.getDoc())
print(pd.getCurso())
pt=Persona('Arnulfo', 3545163157)
pt.setCurso('matematicas')
pt.setCurso('fisica')
print(pt.getNombre())
print(pt.getDoc())
print(pt.getCurso())

print(Persona.Cursos)
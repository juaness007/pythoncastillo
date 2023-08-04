class aprendiz:
    def __init__(self,consecutivo,municipio,colCodIcfes,puntMatematicas,lecturaCritica):
        self.__consecutivo=consecutivo
        self.__municipio=municipio
        self.__colCodIcfes=colCodIcfes
        self.__puntMatematicas=puntMatematicas
        self.__lecturaCritica=lecturaCritica
    def verDatos(self):
        return f"{self.__consecutivo} {self.__municipio} {self.__puntMatematicas} {self.__lecturaCritica}"
    def getConsecutivo(self):
        return self.__consecutivo
    def getmunicipio(self):
        return self.__municipio
    def getpuntMatematicas(self):
        return self.__puntMatematicas
    def getlecturacritica(self):
        return self.__lecturaCritica
    def getcodigoicfes(self):
        return self.__colCodIcfes
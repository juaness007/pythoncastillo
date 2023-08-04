#Escriba un programa que tenga las siguientes funciones:

#1. Crea un archivo nuevo con un nombre que se pasa como parámetro a la función. Valide si el archivo ya existe, en tal caso no lo debe re-crear. Además debe decir cuantas lineas tiene el archivo existente

#2. Solicitar datos personales para guardarlos en un archivo. Se pasa como parámetro el nombre del archivo donde quiere guardar los datos personales. Se ingresan por teclado

#3. Contar los caracteres que contiene un archivo

def crearArchivos(archivo1):
    while True:
        try:
                namefile=input("Introduzca el nombre que le dará al texto:")
                archivo1=open(f'C:\\clon\pythoncastillo\\3Trimestre\\°Samuel')
                archivo1.write(personaldata)
                archivo1.close()
                break  
        except FileExistsError:
            print('El archivo ya existe, intente con otro nombre')   

def personaldata():
    data=input('''Ingrese los siguientes datos
nombres:
apellidos:
edad:
tipo de documento:
numero de documento:
ciudad:''') 
    
    return data                  
            
            
            
            
crearArchivos('')
    
    
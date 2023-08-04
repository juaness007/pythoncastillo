from os import strerror


try:
    stream=open('C:\\clon\\pythoncastillo\\3Trimestre\\Samuel\\ProcessArchivos\\olaa.txt', 'r',encoding='utf-8')
    cont=1
    linea=stream.readline()
    c=1
    while linea !="":
        print(f'{c} {linea}')
        linea=stream.readline()
        c+=1
except IOError as e:
    print(e,'.........')
    
    
 

try:
    counter = 0
    stream = open('C:\\clon\\pythoncastillo\\3Trimestre\\Samuel\\ProcessArchivos\\olaa.txt', "rt",)
    content = stream.read()
    linea=stream.readline()
    while linea !="":
        print(f'{linea} {counter}')
        linea=stream.readline()
        counter+=1
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
    
    
    
    
    
    
    
#    for linea in content:
#         print(linea, end='')
#         counter += 1
#     stream.close()
#     print(f"\n\nEn la linea {linea} hay {counter} caracteres")
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))
   
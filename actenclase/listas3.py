# 3.Llenar un arreglo con la serie de Fibonacci, con la cantidad de dígitos que el usuario
#indique al inicio del programa.

import random
lista=[]
num=int (input("Escriba el numero "))
numero1=0
numero2=1
sol=0   
for m in range (num):
    sol=numero1+numero2
    lista.append(sol)
    numero1=numero2
    numero2=sol
print (lista)
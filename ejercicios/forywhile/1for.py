#Calcular la suma de todos los n numeros enteros ingresados,
#la suma de los pares y la suma de los impares 
cantidad=int(input('Ingrese la cantidad de numeros: '))
suma=0
par=0
impar=0
for i in range (1,cantidad+1):
    num=int(input('Digite el numero: '))
    suma=suma+num
    if num % 2 ==0:
        par=par+num
    else:
        impar=impar+num
print('La suma de todos los numeros es:',suma)
print('La suma de los numeros pares:',par)
print('La suma de los numeros impares: ',impar)    
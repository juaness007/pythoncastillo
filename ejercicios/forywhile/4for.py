#Ingresar 4 notas , mostrarlos en una lista y calcular el promedio

lista=[ ]
suma=0
for i in range(4):
    nota=int(input("Ingrese la nota: "))
    lista.insert(i,nota)
    suma=suma+lista[i]
promedio=suma/4

print(lista)
print("El promedio de las 4 notas es : ",promedio)
#Llenar un arreglo de n elementos con números generados con la función random. N es ingresado por el usuario. Diseñe un menú con las siguientes operaciones.
#a. Imprimir arreglo original (El primero que se generó).
#b. Suma.
#c. Promedio.
#d. Mayor.
# e. Menor.
# f. Ordenar ascendente (No perder el arreglo original; el del punto a).
# g. Ordenar descendente (No perder el arreglo original; el l punto a).
# h. Moda.
# i. Mediana
# j. Buscar. Decir si encuentra el número, en qué posición(es) está, cuantas veces está.
import random
lista=[]
inicio=int(input('ingrese un rango inicial: '))
final=int(input('ingrese un rango final: '))
tam=random.randint(inicio,final)
suma=0
cont=0
mayor=0
menor=100000
print (f'el numero random generado fue {tam}')
for b in range(tam):
    num=random.randrange(10)
    lista.append(num)
print(f'Lista generada de forma random: {lista}')
for c in lista: 
    suma+=c
    cont+=1
num=int(input('ingrese un numero: '))
while num not in lista:
    num=int(input('El numero no se encuentra en la lista, ingrese otro: '))
for b in lista:
    cont=0
    for c in lista:
        if num==c:
            cont+=1
print(f'El numero se encuentra {cont} veces')

for d in range(len(lista)):
    if num==lista[d]:
        print(f'{lista[d]} esta en la posición {d}')
print(f'La suma de los numeros de la lista es {suma}')
promedio=suma/tam
print(f'el promedio de la lista de numeros es {promedio}')
for d in lista:
     if d>mayor:
         mayor=d
     if d<menor:
         menor=d
print(f'El numero mayor es {mayor}')
print(f'el numero menor es {menor}')
for e in range(tam-1):
    for f in range(e+1,tam):
        if lista[e]>lista[f]:
            lista[e],lista[f]=lista[f],lista[e]
print(f'El orden ascedente de la lista es: {lista}')
i=0
for g in lista:
    cont=0
    for h in lista:
        if g==h:
            cont+=1
    if cont>i:
        i=cont
        moda=g
print(f'La moda es {moda}')
for e in range(tam-1):
    for f in range(e+1,tam):
        if lista[e]<lista[f]:
            lista[e],lista[f]=lista[f],lista[e]
print(f'El orden descendente de la lista es: {lista}')
lista_ord=sorted(lista)
long=len(lista_ord)
for med in lista:
    if long %2==0:
        mediana=(lista_ord[int(long/2)-1]+ lista_ord[int(long/2)]) /2
    else:
        mediana = lista_ord[int(long / 2)] 
print(f'la mediana es {mediana}')      
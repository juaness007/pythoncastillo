#tamaño lista (por pueblo): minimo 200 maximo 2500.{validación}
#Llenar Icfes {Resultados. 100 - 500}
#Hallar valor de cada cuartil
#Hallar valor de cada quintil

import random
lista=[]
a=random.randint(100,500)
b=random.randint(200,2500)
def llenarLista(a,b):
    lista=[random.randrange(a) for c in range (b)]
    return lista
l1=llenarLista(a,b)
def lista_ordenada(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
               aux=lista[i]
               lista[i]=lista[j]
               lista[j]=aux
    return lista 

def cuartiles(lista):
    total=[]
    for i in range(4):
        i+=1
        cuartil=i*((len(lista)+1)/4)
        total.append(cuartil)
    return 
def quintiles(lista):
    total=[]
    for i in range(5):
        i+=1
        quintil=i*((len(lista)+1)/5)
        total.append(quintil)
    return total


lista = llenarLista(100, 500)
print("Lista:", l1)
print("Cuartiles:", cuartiles(lista))
print("promedio:", promedio(l1))
print("Quintiles:", quintiles(l1))
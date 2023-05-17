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

#def cuartiles(lista):
#    n = (lista_ordenada)
    #c1 = lista_ordenada[int(n * 0.25)]
   # c2 = lista_ordenada[int(n * 0.5)]
  #  c3 = lista_ordenada[int(n * 0.75)]
 #   return c1, c2, c3
#
def cuartilLista(lista):
    total=[]
    for i in range(4):
        i+=1
        cuartil=i*((len(lista)+1)/4)
        total.append(cuartil)
    return total
def quintiles(lista):
    n = len(lista_ordenada)
    q1 = lista_ordenada[int(n * 0.2)]
    q2 = lista_ordenada[int(n * 0.4)]
    q3 = lista_ordenada[int(n * 0.6)]
    q4 = lista_ordenada[int(n * 0.8)]

    return q1, q2, q3, q4

lista = llenarLista(100, 500)
print("Lista:", l1)
print("Cuartiles:", cuartilLista(lista))
print("promedio:", promedio(l1))
print("Quintiles:", quintiles(l1))
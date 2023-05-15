import random
lista=[]

a=random.randint(1,30)
b=random.randint(5,10)
def llenarLista(a,b):
    lista=[random.randrange(a) for c in range (b)]
    return lista
def sumaLista(lista):
    suma=0
    for d in lista:
        suma+=d
    return suma
def promedioLista(lista):
    return sumaLista(lista)/b
def mayorLista(lista):
    mayor=0
    for e in lista:
        if e>mayor:
            mayor=e
    return mayor
def menorLista(lista):
    menor=1000000
    for f in lista:
        if f<menor:
            menor=f
    return menor
def ascendenteLista(lista):
    for g in range (b-1):
        for h in range(g+1,b):
            if lista[g]>lista[h]:
                lista[g],lista[h]=lista[h],lista[g]
    return lista
def descenteLista(lista):
    for g in range (b-1):
        for h in range(g+1,b):
            if lista[g]<lista[h]:
                lista[g],lista[h]=lista[h],lista[g]
    return lista
l1=llenarLista(a,b)
print(l1)
print(f'La suma de la lista es {sumaLista(l1)}')
print(f'El promedio de la lista es {promedioLista(l1)}')
print(f'El numero mayor de la lista es {mayorLista(l1)}')
print(f'El numero menor de la lista es {menorLista(l1)}')
print(f'El orden ascendente de la lista es: {ascendenteLista(l1)}')
print(f'El orden descendente de la lista es: {descenteLista(l1)}')
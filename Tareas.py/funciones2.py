import random
lista1=[]
lista2=[]
a=random.randint(1,30)
b=random.randint(5,10)

def llenarLista(a,b):
    lista1=[random.randrange(a) for c in range (b)]
    return lista1
l1=llenarLista(a,b)
def llenarLista(a,b):
    lista2=[random.randrange(a) for c in range (b)]
    return lista2
l2=llenarLista(a,b)

def sumaLista(lista1):
    suma=0
    for d in lista1:
        suma+=d
    return suma

def sumaLista(lista2):
    suma=0
    for d in lista2:
        suma+=d
    return suma

def listaMayor(lista1,lista2):
    mayor=0
    for e in range (lista1,lista2):
        if lista2>lista1 or lista1>lista2:
            mayor=e
    return mayor


print(l1)
print(l2)
print(f'La suma de la lista es {sumaLista(l1)}')
print(f'La suma de la lista es {sumaLista(l2)}')
print(f'La lista mayor es {listaMayor(l1,l2)}')


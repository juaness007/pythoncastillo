import random 

lista1=[]
lista2=[]
lista3=[]
a=random.randint(1,20)
b=random.randint(1,10)

def llenarLista(a,b):
    lista1=[random.randrange(a) for c in range (b)]
    return lista1
def llenarLista(a,b):
    lista=[random.randrange(a) for c in range (b)]
    return lista

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

def mayorLista(lista):
    mayor=0
    for e in lista:
        if e>mayor:
            mayor=e
    return mayor

l1=llenarLista(a, b)
l2=llenarLista(a, b)
l3=llenarLista(a, b)

print(l1)
print(l2)
print(f'la suma de la lista 1 es {sumaLista(l1)}')
print(f'la suma de la lista 2 es {sumaLista(l2)}')
print(f'la mayor es {mayorLista(lista)}')

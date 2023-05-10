import random
m=int(input("Digite un numero"))
lista=[]
tam=random.randint(15,20)
print(tam)

for i in range (tam):
    num=random.randrange(0,9)
    lista.append(num)
print(lista)   



for i in range(len(lista)):
    if m == lista[i]:
       print("Si está",m)

for i in range(len(lista)):
    if m == lista[i]:
       print("si esta repetido",)

for i in range(len(lista)):
    if m == lista[i]:
         print (f"{lista [i]} Si esta en la posicion: {i}")
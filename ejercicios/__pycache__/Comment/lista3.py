#Se imorta el modulo random
import random
#Luego creamos una variable 'lista' vacia 
lista=[]
#tammbien creamos una variable 'cuadrado' vacia
cuadrado=[]
#creamos la variable "tam" con la funcion .randint 
#la cual eligirá un numero aleatorio de 5 a 10
tam=random.randint(5,10)
#Se imprime la variable "tam"
print(tam)
#Creamos un bucle for con su respectiva variable
#Que tendra un rango del valor de la variable (tam)
for i in range(tam):
    #Otra variable será creada "num" con el modulo random y la funciom .randrange para asiganarle un rango de 100
    num=random.randrange(100)
    #A la variable "lista " le  agregaremos el valor que tendrá (num)
    lista.append(num)
#Imprimiremos la lista     
print(lista)

#Creamos otro bucle con la misma variable pero esta vez tendrá otra funcion
# El rango será el valor que  tiene la variable 'lista'
for i in range(len(lista)):
    #Agregaremos a la variable cuadrado el total de la operacion
    #Los numeros que se generen en "lista" se multiplican al cuadrado
    cuadrado.append(lista[i]**2)
    #lista[i]=lista[i]**2
    # print(lista[i]*lista[i])
    # print(lista[i]**2)
    # print(math.pow(lista[i],2))
#Se imprimen las dos listas 
print(cuadrado)
print(sum(lista))
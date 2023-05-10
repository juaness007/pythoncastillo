
#immportamos el modulo random
import random
#Creamos una variabñe de tipo entero 
# la cual random.random nos servirá  para generar un numero aleatorio del 1 al 9
num=int(random.random()*10)
#Imprimimos la variable que en este  caso es (num)
print(num)
#Creamos otra  varible donde con el con la funcion random.randint que generará un numero del 0 al 100
num1=random.randint(0,100)
print(num1)
#Creamos una variable con la función .random.randrange 
#la cual servira para generar un numero en un rango de 0 a 10
num2=random.randrange(10)
print(num2)
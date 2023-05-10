#[], {}, (), {()}
#Creamos una variable en este caso x
x=100  
#Luego inprimimos co el tipo de dato de  x
print(type(x))
#Asiganaremos un nuevo valor al la variable
x='Soacha'
print(type(x))
#CCreamos una variable "lista" La cual almacenará daos de diferente tipo 
lista=['python',100,[1,2,3,[]],'a']
#Immprimimos el tipo de la variable lista 
print(type(lista))
#Ahora imprimiremos el numero de datos que hay en la variable lista 
print(len(lista))
#Ahora se imprimirá el dato que esté en la posición del numero que esté dentro ded los corchetes
print(lista[0])
print(lista[1])
print(lista[3])
#Se imprimirá en direccion contraria ya que tiene el signo menos
#Cuando se imprime en reversa se inicia desde el -1
print(lista[-4])
#En este caso la funcion 'del' se utiliza para eliminar un dato
#Se eliminará en la posisción numero :"El que esta dentro de los []"
del lista[-2]
#Y por ultimo se imprime la lista 
print(lista)
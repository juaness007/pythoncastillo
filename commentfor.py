# Utilizamos la funcion "for", la aplicamos a la variable "i" 
# #y range para cuente hasta un determinado numero en este caso 11
for i in range(11):
#Los numero contarán de  0 a 11
    if i%3==0:
        print(f'{i} es multiplo de 3')
#Utilizamos "if" como condición y escribimos la operacion que realizará 
#Luego imprimirá un mensaje si se cumple la operacion         
    else:
        print(i)
#Luego asignamos una variable y la operacion que deberá imprimir 
for j in range(1,11):
    print(j)

for k in range(0,11,2):
    print(k)
#En este caso a diferencia de los otros ponemos el signo resta que servirá para que se impriman los numeros restando
for i in range(20,0,-2):
    print(i)
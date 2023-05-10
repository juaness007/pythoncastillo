#Escribir una frase y contar la cantidad de vocales que aparece en la frase

frase=input('Ingrese la frase que vamos a utilizar: ')
contador=0
for i in frase:
    if i in "aeiou":
        contador=contador+1
print("La cantidad de vocales son: ", contador)        
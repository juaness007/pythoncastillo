#Probando 1 2 3
inicio=int (input('ingrese el numero de inicio: '))
fin=int (input('Ingrese hasta que numero irá la serie: '))
cantidad=int (input('ingrese la cantidad a sumar o restar: '))
n=int(input("Indicar los multiplos de : "))
for a in range(inicio,fin,cantidad):

    if a%n==0:
        print(f"{a} es multiplo de {n}")
    else:print(a)
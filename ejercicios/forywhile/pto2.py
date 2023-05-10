n=int(input('introduzca un numero:'))
cont=0
for a in  range (1,n+1):
    if n % a == 0:
        cont=cont+1
if cont==2:
    print("es primo")
else:
    print("no es primo")      
        
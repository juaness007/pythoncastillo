n=int(input('introduzca un numero:'))

for a in  range (1,n):
    if n % a == 0:
            print(f"{a} es divisor de {n} ")
    else:print(a)
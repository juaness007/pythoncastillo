
  #Lea 2 números. Garantice que hay uno mayor que el otro. Si no es el caso pidalos de nuevo

while True: 

    a=int (input('ingrese un número: '))
    b=int (input('ingrese otro número: '))

    if a==b: 
        print('los números son iguales')
        continue
    else:
        if a>b: print (f'{a} es mayor que {b}') 
        else: print (f'{b} es mayor que {a}')
    break

#Reste el menor del y si el resultado lo permite reste nuevamente. Diga cuanto sobra

if a>b: print(f'La resta de los números {a} y {b} es: {a-b}')
else: print(f'La resta de los números {b} y {a} es: {b-a}')
while True: 

    a=int (input('ingrese un número: '))
    b=int (input('ingrese otro número: '))

    if a==b:
        print('los números son iguales')
        continue
    else:
        if a>b:
            print (f'El {a} es mayor que {b}') 
        else:
            print (f'El {b} es mayor que {a}')
    break
while True: 
    num1=int(input('ingrese numero:'))
    num2=int(input('ingrese numero:'))

    if num1%num2 ==0 or num2%num1 ==0:
        print(f'El {num1} es factor de {num2}')
        break


 #imprimir una serie de 1 hasta n (escrito por usuario)
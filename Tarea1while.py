
while True:
    numero1=int(input('Ingrese  un numero'))
    numero2=int(input('Ingrese  un numero'))
    if numero1==numero2:
        print('los números son iguales')
        continue
    else:
        if numero1>numero2:
            print (f'El {numero1} es mayor que {numero2}') 
        else:
            print (f'El {numero2} es mayor que {numero1}')
    break
    
resultado=0
while True:
   if numero1>numero2 :
        resultado=numero1-numero2 
        print(f"el resultado de la resta de {numero1} y {numero2} es {resultado}")
   else : numero2>numero1
   resultado = numero2 - numero1
   print(f"el resultado de la resta de {numero1} y {numero2} es {resultado}")

   if resultado-numero1:
        while resultado != 0:
            if numero1<numero2:
             resultado= resultado - numero1
            print(f" la diferencia del resutado es {resultado}")
        break    
   #else :numero2>numero1
   #resultado=resultado-numero2
   #print(f" la diferencia del resutado es {resultado}")

  # if resultado<=0:
 #   break

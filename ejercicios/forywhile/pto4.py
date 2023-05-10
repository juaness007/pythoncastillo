#Determinar cuales y cuantos números perfectos hay entre 1 y 1000?
cont=0
sumaDivisores=0
for a in  range (1,1000+1):
 if a % 1000 == 0:
    cont=cont+1

        
   
for b in range (1,1000+1):
    if 1000%b ==0:
        print(f'{b} es perfecto')
    else:print(f'{b} no es perfecto')
sumaDivisores+=b       
if sumaDivisores == 1000:
     True
else:
     False        
        
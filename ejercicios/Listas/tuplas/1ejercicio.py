#llenar una tupla con numeros 1 al 100 
#Con un tamaño de 15 
import random
tam=random.randint(5, 15)
t=()
for i in range (tam):
    n=random.randrange(100)
    t+=(n,)

t2=t[:tam]
t3=t[tam:]    
    
print(t)
print(t2)
print(t3)    
#pendiente terminar
#4. Llenar un arreglo de n elementos con números generados con la función random. No
#puede haber números repetidos. Si intenta ingresar al arreglo un número que ya existe,
#imprimirlo para anunciar que ese número ya está en el arreglo.
 
import random
tam=random.randint(5,10)
n=[random.randrange(10, 20)for i in range (tam)]
print(tam)
print(n)
#for i in range(tam):

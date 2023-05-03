import random

numero_aleatorio = random.randint(1, 100)
intentos = 0

while True:
    intentos += 1
    num = int(input("Adivine el número (entre 1 y 100): "))
    if num == numero_aleatorio:
        print("¡Felicidades! Adivinó el número en", intentos, "intentos.")
        break
    elif num < numero_aleatorio:
        print("El número es más grande.")
    else:
        print("El número es más pequeño.")
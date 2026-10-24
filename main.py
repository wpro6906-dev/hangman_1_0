import random
from palabras import palabras

palabra_secreta = random.choice(palabras)
letras_usadas = []

print("BIENVENIDO AL JUEGO DEL AHORCADO")

while True:
    palabra_mostrada = ""

    for letra in palabra_secreta:
        if letra in letras_usadas:
            palabra_mostrada += letra + " "
        else:
            palabra_mostrada += "_ "

    print("\nPalabra:", palabra_mostrada)

    if "_" not in palabra_mostrada:
        print("¡Felicidades! Ganaste.")
        break

    intento = input("Ingresa una letra: ").upper()

    if len(intento) != 1 or intento < "A" or intento > "Z":
        print("Debes ingresar solo una letra de A a Z.")
        continue

    if intento in letras_usadas:
        print("Ya utilizaste esa letra.")
        continue

    letras_usadas.append(intento)

    if intento in palabra_secreta:
        print("¡Correcto!")
    else:
        print("La letra no está en la palabra.")

import random
from palabras import palabras
from dibujos import dibujos

print("BIENVENIDO AL JUEGO DEL AHORCADO")

while True:
    palabra_secreta = random.choice(palabras)
    letras_usadas = []
    vidas = 6

    while True:
        palabra_mostrada = ""

        for letra in palabra_secreta:
            if letra in letras_usadas:
                palabra_mostrada += letra + " "
            else:
                palabra_mostrada += "_ "

        print("\nPalabra:", palabra_mostrada)
        print("Vidas:", vidas)

        if "_" not in palabra_mostrada:
            print("¡Felicidades! Ganaste.")
            break

        if vidas == 0:
            print("¡Perdiste!")
            print("La palabra era:", palabra_secreta)
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
            vidas -= 1
            print("¡Incorrecto!")
            print(dibujos[6 - vidas])

    while True:
        opcion = input("\n¿Quieres jugar otra vez? (S/N): ").upper()

        if opcion == "S" or opcion == "N":
            break

        print("Opción inválida. Escribe S o N.")

    if opcion == "N":
        print("Gracias por jugar.")
        break

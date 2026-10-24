import random
from palabras import palabras

palabra_secreta = random.choice(palabras)

print("BIENVENIDO AL JUEGO DEL AHORCADO")
print("Adivina la palabra oculta")
print("_ " * len(palabra_secreta))
from random import randint
import os

LIFE_PIKACHU = 10
LIFE_SQUIRTLE = 9

TAMANO_BARRA_VIDA = 20

actual_life_pikachu = LIFE_PIKACHU
actual_life_squirtle = LIFE_SQUIRTLE
placaje = 10
pistola_agua = 12
burbuja = 4
bola_voltio = 7
onda_trueno = 6

while actual_life_pikachu >= 1 and actual_life_squirtle >= 1:
    print("turno pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        print("Pikachu ataca con bola voltio")
        actual_life_squirtle -= bola_voltio
    else:
        print("Pikachu ataca con onda trueno")
        actual_life_squirtle -= onda_trueno

    if actual_life_pikachu < 0:
        actual_life_pikachu = 0
    if actual_life_squirtle < 0:
        actual_life_squirtle = 0

    barras_life_pikachu = int(actual_life_pikachu * TAMANO_BARRA_VIDA / LIFE_PIKACHU)
    barras_life_squirtle = int(actual_life_squirtle * TAMANO_BARRA_VIDA / LIFE_SQUIRTLE)
    print("Pikachu:   [{}{}]  ({}/{})".format("#" * barras_life_pikachu, " " *
                                              (TAMANO_BARRA_VIDA - barras_life_pikachu), actual_life_pikachu, LIFE_PIKACHU))
    print("Squirtle:  [{}{}]  ({}/{})".format("#" * barras_life_squirtle, " " *
                                              (TAMANO_BARRA_VIDA - barras_life_squirtle), actual_life_squirtle, LIFE_SQUIRTLE))

    input("press enter to continue\n\n")
    os.system("cls")

    print("turno squiertle")

    ataque_squirtle = None
    while ataque_squirtle != "a" and ataque_squirtle != "b" and ataque_squirtle != "c":
        ataque_squirtle = input("Que ataque quieres realizar?\n"
                                "a) Placaje\n"
                                "b) pistola agua\n"
                                "c) burbuja\n")
    if ataque_squirtle == "a":
        print("Squirtle ataca con placaje")
        actual_life_pikachu -= placaje
    elif ataque_squirtle == "b":
        print("Squirtle ataca con pistola agua")
        actual_life_pikachu -= pistola_agua
    elif ataque_squirtle == "c":
        print("Squirtle ataca con burbuja")
        actual_life_pikachu -= burbuja

    if actual_life_pikachu < 0:
        actual_life_pikachu = 0
    if actual_life_squirtle < 0:
        actual_life_squirtle = 0

    barras_life_pikachu = int(actual_life_pikachu * TAMANO_BARRA_VIDA / LIFE_PIKACHU)
    barras_life_squirtle = int(actual_life_squirtle * TAMANO_BARRA_VIDA / LIFE_SQUIRTLE)
    print("Pikachu:   [{}{}]  ({}/{})".format("#" * barras_life_pikachu, " " * (TAMANO_BARRA_VIDA - barras_life_pikachu),
                                              actual_life_pikachu, LIFE_PIKACHU))
    print("Squirtle:  [{}{}]  ({}/{})".format("#" * barras_life_squirtle, " " * (TAMANO_BARRA_VIDA - barras_life_squirtle),
                                              actual_life_squirtle, LIFE_SQUIRTLE))

    input("press enter to continue\n\n")
    os.system("cls")

if actual_life_squirtle > actual_life_pikachu:
    print("Squirtle gana la partida")
else:
    print("Pikachu gana la partida")

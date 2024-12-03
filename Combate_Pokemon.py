from random import randint
import os


VIDA_INICIAL_PIKACHU = 120 #Controlado por la CPU
VIDA_INICIAL_SQUIRTLE = 20 #Controlado por humano
TAMAÑO_BARRA_VIDA = 20
vida_pikachu = VIDA_INICIAL_PIKACHU
vida_pikachu = max(vida_pikachu, 0)
vida_squirtle = VIDA_INICIAL_SQUIRTLE
vida_squirtle = max(vida_squirtle, 0)

while vida_pikachu > 0 and vida_squirtle > 0:
    #Empieza el combate por turnos

    #Turno del pikachu (CPU)
    print("turno del pikachu")
    ataque_pikachu = randint(1,2)
    # 1=bola voltio [10 daño] / 2=impact trueno [12 daño]
    if ataque_pikachu == 1:
        print("Pikachu ataca con Vola Voltio")
        vida_squirtle -= 10
        # (vida_squirtle -= 10) es lo mismo que (vida_squirtle = vida_squirtle -10)
    else:
        print ("Pikachu ataca con Impact Trueno")
        vida_squirtle -= 12

    if vida_pikachu < 0:
        vida_pikachu = 0

    elif vida_squirtle < 0:
        vida_squirtle = 0

    barra_de_vida_pikachu = int(vida_pikachu * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
    print("Pikachu:  [{}{}]".format("*" * barra_de_vida_pikachu, " " * (TAMAÑO_BARRA_VIDA - barra_de_vida_pikachu)) +
          f" ({vida_pikachu}/{VIDA_INICIAL_PIKACHU})")
    barra_de_vida_squirtle = int(vida_squirtle * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle: [{}{}]".format("*" * barra_de_vida_squirtle, " " * (TAMAÑO_BARRA_VIDA - barra_de_vida_squirtle)) +
          f" ({vida_squirtle}/{VIDA_INICIAL_SQUIRTLE})")

    input("Pulsa Enter para continuar")

    os.system('cls')

    #Turno del Squirtel (HUMANO)
    print("Turno de Squirtle")

    ataque_squirtle = None
    while (ataque_squirtle not in ["placaje", "pistola agua", "burbujas", "no hacer nada"]):
        ataque_squirtle = input("Que ataque quieres hacer? [Placaje] [Pistola Agua] [Burbuja] [No hacer nada]")
        if ataque_squirtle == "placaje":
            vida_pikachu -= 10
        elif ataque_squirtle == "pistola agua":
            vida_pikachu -= 12
        elif ataque_squirtle == "burbuja":
            vida_pikachu -= 9
        elif ataque_squirtle == "no hacer nada":
            print("Squirtle no ha hecho nada...")

    if vida_pikachu < 0:
        vida_pikachu = 0

    elif vida_squirtle < 0:
        vida_squirtle = 0

    barra_de_vida_pikachu = int(vida_pikachu * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
    print("Pikachu:  [{}{}]".format("*" * barra_de_vida_pikachu, " " * (TAMAÑO_BARRA_VIDA - barra_de_vida_pikachu)) +
          f" ({vida_pikachu}/{VIDA_INICIAL_PIKACHU})")
    barra_de_vida_squirtle = int(vida_squirtle * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)

    print("Squirtle: [{}{}]".format("*" * barra_de_vida_squirtle, " " * (TAMAÑO_BARRA_VIDA - barra_de_vida_squirtle)) +
          f" ({vida_squirtle}/{VIDA_INICIAL_SQUIRTLE})")

    input("Pulsa Enter para continuar")

    os.system('cls')

if vida_pikachu > vida_squirtle:
    input("pikachu gana")
elif vida_pikachu < vida_squirtle:
    input("squirtle gana")
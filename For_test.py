#CONTADOR DE VOCALES CON FUNCIÓN FOR:

vocales = ["a", "e", "i", "o", "u"]
frase = "hola, cuenta cuantas vocales hay en esta frase"
numero_vocales = 0

for letra in frase:
    if letra in vocales:
        numero_vocales += 1

print(f"vocales encontradas: {numero_vocales}")


#REPETIDOR DE PALABRAS CON LA FUNCIÓN FOR:

numero_de_repeticiones = int(input("¿Cuantas veces quieres repetir el mensaje 'hola'?: "))

for a in range(numero_de_repeticiones):
    print("hola")

#CONTADOR DE ESPACIOS, PUNTOS Y COMAS:

espacios = " "
puntos = "."
comas = ","
numero_espacios = 0
numero_puntos = 0
numero_comas = 0

frase = input("escribe una frase para contar los espacios, puntos y comas: ")

for letra in frase:
    if letra in espacios:
        numero_espacios += 1
    elif letra in puntos:
        numero_puntos += 1
    elif letra in comas:
        numero_comas += 1

print(f"hay {numero_espacios} espacios, {numero_puntos} puntos y {numero_comas} comas en la frase")


#TABLA DE MULTIPLICAR EN BASE A UN NUMERO ELEGIDO:

numero = int(input("Que tabla de multiplicar quieres:"))

for n in range(1, 11):
    print(f"{n} x {numero} = {n * numero}")
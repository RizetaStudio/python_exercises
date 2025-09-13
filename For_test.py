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

space = " "
point = "."
coma = ","
count_space = 0
count_point = 0
count_coma = 0

input_user = input("ingrese una frase")

for item in input_user:
    if item in space:
        count_space += 1

    elif item in point:
        count_point += 1

    elif item in coma:
        count_coma += 1

print("he encontrado {} espacios, {} puntos y {} comas".format(count_space, count_point, count_coma))


#TABLA DE MULTIPLICAR EN BASE A UN NUMERO ELEGIDO:

numero = int(input("Que tabla de multiplicar quieres:"))

for n in range(1, 11):

    print(f"{n} x {numero} = {n * numero}")

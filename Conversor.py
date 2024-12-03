
inicio = input ("elige una transacción de moneda\n"
                "a: convertir de Euro a Dolar\n"
                "b: convertir de Dolar a Euro\n"
                "c: convertir de Euro a Libra\n"
                "d: convertir de Libra a Euro\n")

if inicio == "a":
    euro = float(input("Que cantidad de Euros quieres convertir a Dolares?"))
    euro_a_dolar = (euro / 0.91)
    input("Has cambiado {}€ a {}$, ".format(euro, euro_a_dolar) + "pulsa ENTER para finalizar" + "\n")
    input("estás seguro de cerrar el programa? Pulsa ENTER para confirmar" + "\n")
    exit()

elif inicio == "b":
    dolar = float(input("Que cantidad de Dolares quieres convertir a Euros?"))
    dolar_a_euro = (dolar * 0.91)
    input("Has cambiado {}$ a {}€, ".format(dolar, dolar_a_euro) + "pulsa Enter para finalizar" + "\n")
    input("estás seguro de cerrar el programa? Pulsa ENTER para confirmar" + "\n")
    exit()

elif inicio == "c":
    euro_lib = float(input("Que cantidad de Euros quieres convertir a Libras?"))
    euros_a_libras = (euro_lib / 1.18)
    input("Has cambiado {}€ a {} libras, ".format(euro_lib, euros_a_libras) + "pulsa ENTER para finalizar" + "\n")
    input("estás seguro de cerrar el programa? Pulsa ENTER para confirmar" + "\n")
    exit()

elif inicio == "d":
    libra = float(input("Que cantidad de Libras quieres convertir a Euros?"))
    libra_a_euro = (libra * 1.18)
    input("Has cambiado {} libras a {}€, ".format(libra, libra_a_euro) + "pulsa ENTER para finalizar\n")
    input("estás seguro de cerrar el programa? Pulsa ENTER para confirmar" + "\n")
    exit()

else:
    input("tenías que seleccionar una opción entre la a y la c, pulsa ENTER para terminar" + "\n")
    exit()


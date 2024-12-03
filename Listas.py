
lista_compra = []
producto = None

while producto != "q":
    producto = input("¿Que desea comprar? ([Q] para salir): ")
    if producto == "q":
        pass
    elif producto not in lista_compra:
        confirmacion = input(f"¿Seguro que quieres añadir {producto} a la lista de la compra? ")
        if confirmacion == "si":
            lista_compra.append(producto)
            print(f"has añadido {producto} a la lista de la compra")
        else:
            print(f"no se ha añadido {producto} a la lista de la compra")
    elif producto in lista_compra:
        print("Este producto ya lo tienes en la lista de la compra")


input(f"esta es la lista de la compra: \n {lista_compra} \nPulsa 'ENTER' para salir")


print("Bienvenido al programa para comprobar si puedes optar al descuento para los Cines Garracho")
edad = int(input("Primero de todo, ¿Que edad tienes?"))
tipo_carnet = input("""¿Que tipo de carnet tienes?
    e = Estudiante
    p = Pensionista
    f = Familia numerosa
    n = Ningún carnet
Solo tienes que seleccionar la letra: """)

if ((25 < edad < 35 and tipo_carnet == "e") \
        or edad <10 \
        or (edad > 65 and tipo_carnet == "p") \
        or (tipo_carnet == "f")):
    input("tienes disponible un descuento del 25%")

else:
    input("lo sentimos, no tienes descuento para tu entrada")

#----------------INFORMACIÓN INTERNA---------------
pregunta_dinero = "¿Quieres un móvil de alta gama? responde con 'Si' o 'No': \n"
pregunta_so = "¿Que sistema operativo prefieres en tu móvil? ¿Andorid o IOS?\n"
pregunta_ia = "¿Quieres un movil que incorpore inteligencia artificial? Responde con 'Si' o 'No': \n"
respuesta_movil = "después de estudiar todas las variables posibles, la mejor opción para ti es el {} con un precio de {}, pulsa 'ENTER' para continuar\n"
error = "No has seleccionado ningún sistema operativo, pulsa 'ENTER' para cerrar el programa: "
despedida = "Muchas gracias por participar en este test para saber el móvil que necesitas, pulsa 'ENTER' para finalizar: \n"
despedida_confirmacion = "¿Seguro que quieres cerrar el progama? Pulsa 'ENTER' para cerrarlo definitivamente: "

#Listado de precios según modelo
precio_ip15 = "849€" #iphone 15 pro
precio_ipse = "382€" #iphone SE
precio_xiao = "599€" #Xiaomi Mi 13 Lite
precio_goog = "779€" #Google Pixel 10
precio_remi = "249€" #Redmi Lomid 12
#Listado de móviles disponibles
iphone_15 = "Iphone 15 Pro"
iphone_se = "Iphone Se"
xiaomi_mi = "Xiaomi Mi 13"
google_px = "Google Pixel 10"
redmi_low = "Redmi lomid 12"
#--------------------PROGRAMA---------------------
titulo= "Bienvenido al test para elegir tu nuevo teléfono móvil"

input(titulo + "\n" + "_" * len(titulo) + ("\n" * 2) + "Pulsa 'Enter' para empezar:\n")

so = input(pregunta_so)
if so == "android":
    dinero = input(pregunta_dinero)
    if dinero == "si":
        ia = input(pregunta_ia)
        if ia == "si":
            input(respuesta_movil.format(google_px, precio_goog))
        elif ia == "no":
            input(respuesta_movil.format(xiaomi_mi, precio_xiao))
    elif dinero == "no":
        input(respuesta_movil.format(redmi_low, precio_remi))
    input(despedida)
    input(despedida_confirmacion)
    exit()
if so == "ios":
    dinero = input(pregunta_dinero)
    if dinero == "si":
        input(respuesta_movil.format(iphone_15, precio_ip15) + "\n")
    elif dinero == "no":
        input(respuesta_movil.format(iphone_se, precio_ipse) + "\n")
    input(despedida)
    input(despedida_confirmacion)
    exit()
else:
    input(error)
exit()

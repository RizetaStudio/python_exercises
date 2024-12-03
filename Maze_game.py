import os
import readchar
import random

#CREACIÓN DEL MAPA Y POSICIÓN DEL JUGADOR

POS_X = 0
POS_Y = 1
NUM_OF_OBJECTS_IN_MAP = 11 # Numero de objetos que habrá en el mapa
my_position = [5, 6] # posición X y posición Y
tail_lenght = 0
tail = []
map_objects = []
obstacle_definition = """"\
#####                           
#####                              
#####                               
#####                               
                                    
                                    
                                    
            #########               
            #########               
               ##                   
                                    
                                    
                                    
                              ######
                              ######
                        ############
                        ############\
"""

end_game = False
died = False

#CREATE OBSTACLE MAP
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_WIDTH = len(obstacle_definition[0]) # X - ancho de mapa
MAP_HEIGHT = len(obstacle_definition) # Y - alto de mapa

#MAIN LOOP (BUCLE PRINCIPAL)
while not end_game:
    os.system("cls")

    # GENERATE RANDOM OBJECTS ON THE MAP
    while len(map_objects) < NUM_OF_OBJECTS_IN_MAP:
        new_position = [random.randint(0, MAP_WIDTH), random.randint(0, NUM_OF_OBJECTS_IN_MAP)]

        if new_position not in map_objects and new_position != my_position:
            map_objects.append(new_position)

    # DIBUJAR MAPA
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for cordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for cordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == cordinate_x and map_object[POS_Y] == cordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object

            for tail_piece in tail:
                if tail_piece[POS_X] == cordinate_x and tail_piece[POS_Y] == cordinate_y:
                    char_to_draw = "="
                    tail_in_cell = tail_piece

            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                char_to_draw = "@"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_lenght += 1

                if tail_in_cell:
                    print("Has muerto")
                    end_game = True

            if obstacle_definition[cordinate_y][cordinate_x] == "#":
                char_to_draw = "#"


            print(f" {char_to_draw} ", end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    print(f"tamaño de la cola {tail_lenght}")
    print(tail)


    #CREACION DEL MOVIMIENTO DEL PERSONAJE

    #direction = input("¿Donde te quieres mover? [WASD]: ")

    direction = readchar.readchar()
    new_position = None

    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]

    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]

    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "p":
        end_game = True

    if new_position:
        # Verifica si la nueva posición no es un obstáculo
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_lenght]
            # Actualizar ambas coordenadas X e Y
            my_position[POS_X] = new_position[POS_X]
            my_position[POS_Y] = new_position[POS_Y]

    os.system("cls")

    if died:
        print("has muerto")
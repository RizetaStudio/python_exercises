import os
import random
from readchar import readchar

POS_X = 0
POS_Y = 1
NUM_MAP_OBJECTS = 11

obstacle_definition = """\
                                      
    ############                       ########
         ##                            ##     
         ##                            ##
    ############   ##################  ###        
    ############                       #######
              ##   ##################  ###      
              ##                       ##
         #######                       ##
         ###############               ########
"""

my_position = [8, 8]  # [x, y]
tail = []
map_objects = []
tail_length = 0

end_game = False
died = False

# Convertir a lista de listas y normalizar filas
rows = obstacle_definition.split("\n")
MAP_WIDTH = max(len(row) for row in rows)
MAP_HEIGHT = len(rows)

obstacle_definition = [list(row.ljust(MAP_WIDTH)) for row in rows]

while not end_game:
    os.system("cls" if os.name == "nt" else "clear")

    # Crear objetos en el mapa
    while len(map_objects) < NUM_MAP_OBJECTS:
        new_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]
        if (new_position not in map_objects and
            new_position != my_position and
            obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#"):
            map_objects.append(new_position)

    print("+" + "-" * (MAP_WIDTH * 2) + "+")

    for y in range(MAP_HEIGHT):
        print("|", end="")
        for x in range(MAP_WIDTH):
            char_to_draw = "  "
            object_in_cell = None
            tail_in_cell = None

            for item in map_objects:
                if item[POS_X] == x and item[POS_Y] == y:
                    char_to_draw = "* "
                    object_in_cell = item

            for tail_piece in tail:
                if tail_piece[POS_X] == x and tail_piece[POS_Y] == y:
                    char_to_draw = "o "
                    tail_in_cell = tail_piece

            if my_position[POS_X] == x and my_position[POS_Y] == y:
                char_to_draw = "@ "
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1
                if tail_in_cell:
                    end_game = True
                    died = True

            if obstacle_definition[y][x] == "#":
                char_to_draw = "XX"

            print(char_to_draw, end="")
        print("|")
    print("+" + "-" * (MAP_WIDTH * 2) + "+")
    print("Tamaño de la cola: {}".format(tail_length))

    direction = readchar()
    new_position = None

    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]
    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]
    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]
    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]
    elif direction == "q":
        end_game = True

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position = new_position

if died:
    print("Has muerto porque te has mordido la cola de {} metros".format(tail_length))


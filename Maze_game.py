import os
import random
from readchar import readchar

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20 #ancho
MAP_HEIGHT = 15 #alto
NUM_MAP_OBJECTS = 11


my_position = [8, 8] # [x, y]
tail = []
map_objects = []
tail_lenght = 0

end_game = False
died = False

while not end_game:
    os.system("cls")

    while len(map_objects) < NUM_MAP_OBJECTS:
        new_position = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]
        if new_position not in map_objects and new_position != my_position:
            map_objects.append(new_position)

    print("+" + "-" * (MAP_WIDTH * 3) + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print ("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None

            for item in map_objects:
                if item[POS_X] == coordinate_x and item[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = item

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = "o"
                    tail_in_cell = tail_piece

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_lenght += 1

                if tail_in_cell:
                    end_game = True
                    died = True

            print(" {} ".format(char_to_draw), end="")


        print("|")
    print("+" + "-" * (MAP_WIDTH * 3) + "+")
    print("tamaño de la cola {}".format(tail_lenght))

    direction = readchar()
    if direction == "w":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "s":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "a":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "q":
        end_game = True



if died == True:
    print("Has muerto porque te has mordido la cola de {} metros".format(tail_lenght))

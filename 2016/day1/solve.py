
import numpy as np



# FUNCTION 0
# Split the direction and number as two separate characters
def parse_direction(character):
    direction = character[0]
    number = int(character[1:])
    return direction, number



# Functions to determine which direction you are currently facing
# Input previous direction and output which direction you end up after turning

# mapping between input and output

# left is -1 and right is +1
# if new position at 0 then set to last position on array
# if new position at 4 then set to first position on array
directions = [ 'W', 'N', 'E', 'S' ]

def adj_direction_position(new_pos, drections):
    if new_pos == -1:
        new_pos = len(directions) - 1
    elif new_pos == len(directions):
        new_pos = 0
    return directions[new_pos]


def find_new_direction(direction, turn):
    old_pos = directions.index(direction)
    move = -1 if turn=="L" else +1
    new_pos = old_pos + move
    new_direction =  adj_direction_position(new_pos, directions)
    return new_direction



# Determine the x, y coordinates of your destination
# based on the direction you are starting at, the direction you are heading
# and how far you end up

# update the coordinates based on old coordinates, direction and steps
def update_coordinates(old_coord, direction, steps):
    x = old_coord[0]
    y = old_coord[1]
    if direction == "E":
        new_coord = [x + steps, y]
    if direction == "W":
        new_coord = [x - steps, y]
    if direction == "N":
        new_coord = [x, y + steps]
    if direction == "S":
        new_coord = [x, y - steps]
    return new_coord


# translate character in input into new coordinates
def find_new_coordinates(direction, old_coord, character):
    direction_tuple = parse_direction(character)
    turn = direction_tuple[0]
    steps = direction_tuple[1]
    new_direction = find_new_direction(direction, turn)
    new_coord  = update_coordinates(old_coord, new_direction, steps)
    return new_direction, new_coord


# iterate through the input directions
# read in the array of directions and translate into final coordinate
def read_directions(directions):
    coord = [0,0]
    direction = "N"
    for instr in directions:
        print("UPDATE " + instr)
        output = find_new_coordinates(direction, coord, instr)
        direction = output[0]
        coord = output[1]
        print(direction)
        print(coord)
    return coord

# read the input and output coordinate
with open ("input", "r") as input:
    data=input.read()
    new_data = data.split(', ')
    new_direction = read_directions(new_data)

# Final coordinates [164, -136]
# 164 + 136 = 300 blocks



# Comments from Peter Norvig's solution
# He used a complex number system to define the directions
# N, S, E, W = 1j, -1j, 1, -1
# Turns = L, R = 1j, -1j
# so turning right facing North, takes you to 1j * -1j = 1 (East)
# so turning left facing North, takes you to 1j * 1j = -1 (West)
# so turning right on East, takes you to 1 * -1j = -1j (South)
# so turning left on East, takes you to 1 * 1j = 1j (North)

# Using the complex number system for mapping
# you can multiply the complex number by the number of steps to figure
# out the total number of steps in that direction





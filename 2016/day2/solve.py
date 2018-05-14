import numpy as np


# If the position is outside the range of possible
# set it to limit
def map_to_possible(number):
    if number<0:
        output = 0
    elif number>2:
        output = 2
    else:
        output = number
    return output

def map_array(array):
    new_array = [ map_to_possible(array[0]), 
        map_to_possible(array[1])]
    return(new_array)


def sum_array(array1, array2):
    new_array = [ array1[0] + array2[0], 
         array1[1] + array2[1]]
    return(new_array)


# matrix repesenting the bathroom keys
mat = np.matrix('1 2 3; 4 5 6; 7 8 9')

# the shift in position
movement ={
    "U" : np.array([-1,0]),
    "D" : np.array([1,0]),
    "L" : np.array([0,-1]),
    "R" : np.array([0,1]),
}


pos = np.array([1,1])
# read the input and output coordinate
with open ("input", "r") as input:
    number = []
    lines = input.read().splitlines()
    for line  in lines:
        print "NEXT:" + line
        for direction in line:
            print "Movements"
            print(pos)
            print(shift)
            shift = movement[direction]
            pos = sum_array(pos , shift)
            pos = map_array(pos)
            print pos
        number.append(mat[pos[0], pos[1]])
        print number



# Peter Norvig's solution
# https://nbviewer.jupyter.org/url/norvig.com/ipython/Advent%20of%20Code.ipynb
# use arrays instead of matrix
# Keypad = str.split
# keypad = Keypad("""
# .....
# .123.
# .456.
# .789.
# .....
# """)

# set dead areas around the matrix "."
# if the next outcome is "." then don't move

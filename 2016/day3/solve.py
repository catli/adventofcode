import numpy as np

# Get the max number
# Find the remainder 

def remove_blanks(input):
    new = [s for s in input if s!='' ]
    # remove extra space
    new = [int(n) for n in new]
    # convert to integer
    return new


def compare_sides(side, other):
    is_triangle = False
    if other>side:
        is_triangle = True
    return is_triangle

def sum_nonmax(array):
    max_side = np.amax(array)
    other_sides = np.sum(array) - max_side
    return compare_sides(max_side, other_sides)



with open ("input.txt", "r") as input:
    number = []
    lines = input.readlines()
    count = 0
    for line in lines:
        numbers = line.split(' ')
        new_numbers = remove_blanks(numbers)
        print new_numbers
        count+=sum_nonmax(new_numbers)
        print count
    print count
        # for number in numbers:
        #     print int(number)

    
# answer: 858
# Peter Norvig Solution
# sorted the sides
# x, y, z = sorted(sides)
# return z < x + y





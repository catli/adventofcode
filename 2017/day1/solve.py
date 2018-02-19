import numpy as np

with open ("input", "r") as input:
    data=input.readlines()
    numba = data[0]

    # starting seed is last number in the string
    last = numba[-1]
    array = []

    print numba
    for a in numba:
        if last == a:
            array.append(int(last))
        last = a

    print array
    print np.sum(array)


# the answer is 1089
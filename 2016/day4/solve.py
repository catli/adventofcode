import numpy as np


# extract check sum
def extract_checksum(line):
    new_lines = line.split('[')
    code =  new_lines[0]
    checksum = new_lines[1].split(']')[0]
    return code, checksum

# etract sector id
def extract_sector(code):
    return code.split('-')[-1]


# table, group by alphabets and count
# ordr by count desc than alphabets
# WHAT IS THE BEST WAY TO SORT ALONG TWO VARS IN PYTHON
# DICTIONARY

# does the first 5 alphabet match the checksum
# if so add sector id to real room array


# sum all sectors in the array

with open ("input.txt", "r") as input:
    realnumber = []
    lines = input.readlines()
    for line in lines:
        code, checksum = extract_checksum(line)
        sector_id = extract_sector(code)
        # group code and count
        # if match check sum add to realnumber
    print np.sum(realnumber)
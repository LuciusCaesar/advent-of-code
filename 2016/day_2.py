"""Script for Day 2 Advent Calendar of 2016"""
import math

# instructions = [
#     "ULL",
#     "RRDDD",
#     "LURDL",
#     "UUUUD"
# ]

instructions = []
with open("day_2_input.txt", "r") as f:
    content = f.readlines()
    for line in content:
        instructions.append(line.rstrip())

moves = {
    "U": 1j,
    "D": -1j,
    "R": 1,
    "L": -1
}

key_pad_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def find_key_3x3(pad, z:complex) -> int:
    """
    Find the key from a complex number representing its position
    The origin (z=0+0j) means the center of the 3x3 pad
    """
    return pad[-int(z.imag + 2)][int(z.real + 1)]

key_pad_2 = [
    [0, 0, 1, 0, 0],
    [0, 2, 3, 4, 0],
    [5, 6, 7, 8, 9],
    [0, "A", "B", "C", 0],
    [0, 0, "D", 0, 0]
]

def find_key_5x5(pad, z:complex) -> int:
    """
    Find the key from a complex number representing its position
    The origin (z=0+0j) means the center of the 5x5 pad
    """
    return pad[-int(z.imag + 3)][int(z.real + 2)]


#position = 0 #for part 1
#distance = math.sqrt(2)
position = complex(-2, 0) #for part 2
distance = 2

code = []
for line in instructions:
    for letter in line:
        new_position = position + moves[letter]
        if abs(new_position) <= distance: #check that we don't get out of the pad, otherwise we don't update the position
            position = new_position
    # code.append(find_key_3x3(key_pad_1, position))
    code.append(find_key_5x5(key_pad_2, position))

print(code)

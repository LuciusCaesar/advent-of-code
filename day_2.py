"""Script for Day 2 Advent Calendar of 2016"""
import math

instructions = [
    "ULL",
    "RRDDD",
    "LURDL",
    "UUUUD"
]

moves = {
    "U": 1j,
    "D": -1j,
    "R": 1,
    "L": -1
}

key_pad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def find_key(pad, z:complex) -> int:
    """
    Find the key from a complex number representing its position
    The origin (z=0+0j) means the center of the 3x3 pad
    """
    return pad[-int(z.imag + 2)][int(z.real + 1)]

code = []
position = 0
for line in instructions:
    for letter in line:
        new_position = position + moves[letter]
        if abs(new_position) <= math.sqrt(2): #check that we don't get out of the pad, otherwise we don't update the position
            position = new_position
    code.append(find_key(key_pad, position))

print(code)

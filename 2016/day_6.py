"""Module to solve Day 6 of 2016"""
from collections import Counter

with open("2016/day_6_input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

message = ""
for i in range(len(lines[0])):
    column = [line[i] for line in lines]
    
    # c = Counter(column).most_common()
    c = Counter(column).most_common()
    # message += c[0][0]
    message += c[-1][0]

print(message)
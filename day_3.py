"""Day 3 of the 2016 AoC"""

instructions = []
with open("day_3_input.txt", "r") as f:
    content = f.readlines()
    for line in content:
        instructions.append(line.strip().split())
    

def is_valid_sums(dimensions:list) -> bool:
    """Returns False triangular inequality is not respected in the set of three numbers"""
    result = True
    i = 0
    while i < 4:
        a = i%3
        b = (i+1)%3
        c = (i+2)%3
        if int(dimensions[a]) + int(dimensions[b]) <= int(dimensions[c]): #TODO: would be best to firt prepare the data instead of casting them here
            result = False
            break
        i+=1
    return result

number_of_valid_triangles = 0
for triangle in instructions:
    if is_valid_sums(triangle):
        number_of_valid_triangles += 1

print(number_of_valid_triangles)
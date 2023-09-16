"""Day 5 of 2016 Problem"""
import hashlib

input = "cxdnnyjw"
# input = "abc"
found = False

def get_hash(input: str):
    return hashlib.md5(input.encode()).hexdigest()

def find_next_index(input: str, index = -1) -> int:
    index += 1
    hash = get_hash(input + str(index))

    while(not hash.startswith("00000")):
        index += 1
        hash = get_hash(input + str(index))
    
    return index, hash

index = -1
code = ["", "", "", "", "", "", "", ""]
while("" in code):
    index, hash = find_next_index(input, index)
    if(hash[5].isdigit() and int(hash[5]) < 8 and code[int(hash[5])] == ""):
        print([index, hash,hash[5],hash[6]])
        code[int(hash[5])] = hash[6]
        print("".join(code))
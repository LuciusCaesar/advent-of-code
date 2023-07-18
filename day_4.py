"""Day 4 2016 or AoC"""
alphabet = "abcdefghijklmnopqrstuvwxyz"

line = "aaaaa-bbb-z-y-x-123[abxyz]"

sector_id = line.split('-').pop(-1).split('[')[:-1][0]
print(sector_id)
checksum = line.split('-').pop(-1).split('[')[1][:-1]
print(checksum)
# name = line.removesuffix(']').removesuffix(checksum).removesuffix('[').
name = line.removesuffix('-' + sector_id + '[' + checksum + ']')
print(name)


def is_valid_line(line:str) -> tuple:
    checksum = extract_checksum(line)
    sector = extract_sector_id(line)
    name = extract_name(line, sector, checksum)

    return (is_name_and_checksum_consistant(name, checksum), sector)

def is_name_and_checksum_consistant(name:str, input_checksum:str) -> bool:
    """Returns true if name and checksum are consistent"""
    letter_occurences = [(name.count(letter), letter) for letter in alphabet if name.count(letter) > 0]
    sorted_letter_occurences = sorted(letter_occurences, key= lambda x : (-x[0], x[1]))
    calculated_checksum = ''.join([x[1] for x in sorted_letter_occurences])[0:5]

    return input_checksum == calculated_checksum

def extract_name(line:str, sector_id:int, checksum:str) -> str:
    """Extract the name by removing the information at ends of line"""
    return line.removesuffix('-' + sector_id + '[' + checksum + ']')

def extract_checksum(line:str) -> str:
    """Extract checksum"""
    return line.split('-').pop(-1).split('[')[1][:-1]

def extract_sector_id(line:str) -> int:
    """Extract sector_id"""
    return line.split('-').pop(-1).split('[')[:-1][0]

checklist = []
with open("day_4_input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        checklist.append(is_valid_line(line.strip()))

real_rooms = [room for room in checklist if room[0]]
total_sectors = sum([int(room[1]) for room in real_rooms])
print(total_sectors)
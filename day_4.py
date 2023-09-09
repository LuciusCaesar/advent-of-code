"""Day 4 2016 or AoC"""
alphabet = "abcdefghijklmnopqrstuvwxyz"

# line = "aaaaa-bbb-z-y-x-123[abxyz]"

# sector_id = line.split("-").pop(-1).split("[")[:-1][0]
# checksum = line.split("-").pop(-1).split("[")[1][:-1]
# # name = line.removesuffix(']').removesuffix(checksum).removesuffix('[').
# name = line.removesuffix("-" + sector_id + "[" + checksum + "]")


def get_room_from_line(line: str) -> tuple:
    """Return the room details from input file's lines"""
    checksum = extract_checksum(line)
    sector_id = extract_sector_id(line)
    name = extract_name(line, sector_id, checksum)

    # return (is_name_and_checksum_consistant(name, checksum), sector)
    return {
        "is_valid_room": is_name_and_checksum_consistant(name, checksum),
        "name": name,
        "sector_id": sector_id,
        "checksum": checksum,
    }


def is_name_and_checksum_consistant(name: str, input_checksum: str) -> bool:
    """Returns true if name and checksum are consistent"""
    letter_occurences = [
        (name.count(letter), letter) for letter in alphabet if name.count(letter) > 0
    ]
    sorted_letter_occurences = sorted(letter_occurences, key=lambda x: (-x[0], x[1]))
    calculated_checksum = "".join([x[1] for x in sorted_letter_occurences])[0:5]

    return input_checksum == calculated_checksum


def extract_name(line: str, sector_id: int, checksum: str) -> str:
    """Extract the name by removing the information at ends of line"""
    return line.removesuffix("-" + sector_id + "[" + checksum + "]")


def extract_checksum(line: str) -> str:
    """Extract checksum"""
    return line.split("-").pop(-1).split("[")[1][:-1]


def extract_sector_id(line: str) -> int:
    """Extract sector_id"""
    return line.split("-").pop(-1).split("[")[:-1][0]


def shift_letter(letter: str, cipher: int) -> str:
    """Return the letter shifted in the alphabet"""
    if letter in [" ", "-", "_"]:
        return letter
    return alphabet[(alphabet.index(letter) + cipher) % len(alphabet)]


def unencrypt(word: str, cipher: int) -> list:
    """unencrypt a word"""
    return [shift_letter(letter, cipher) for letter in word]


rooms = []
with open("day_4_input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        rooms.append(get_room_from_line(line.strip()))

# real_rooms = [room for room in rooms if room["is_valid_room"]]

# unencrypted_rooms = [unencrypt(room["name"], room["sector_id"]) for room in real_rooms]
unencrypted_rooms = [
    ("".join(unencrypt(room["name"], int(room["sector_id"]))), room["sector_id"])
    for room in rooms
    if room["is_valid_room"]
]

cancidates = [
    room
    for room in unencrypted_rooms
    if ("north" in room[0])
]

print(cancidates)

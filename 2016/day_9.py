"""module to treat day 9 2016 AoC"""
import re


with open("2016/day_9_input.txt", "r") as file:
    file_contents = [line.strip() for line in file.readlines()]

file_compressed_content = file_contents[0]


def calculate_uncompressed_size(compressed_content: str) -> int:
    """
    >>> calculate_uncompressed_size("ADVENT")
    6

    >>> calculate_uncompressed_size("A(1x5)BC")
    7

    >>> calculate_uncompressed_size("(3x3)XYZ")
    9

    >>> calculate_uncompressed_size("A(2x2)BCD(2x2)EFG")
    11

    >>> calculate_uncompressed_size("(6x1)(1x3)A")
    6

    >>> calculate_uncompressed_size("X(8x2)(3x3)ABCY")
    18
    """
    size = 0
    cursor = 0
    remaining_content = compressed_content

    match = re.search(r"\((\d+)x(\d+)\)", remaining_content)
    while match is not None:
        start = match.start()
        end = match.end()

        size += match.start() + (int(match.group(1)) * int(match.group(2)))
        cursor = match.end() + int(match.group(1))
        remaining_content = remaining_content[cursor:]
        match = re.search(r"\((\d+)x(\d+)\)", remaining_content)

    size += len(remaining_content)
    return size


print(calculate_uncompressed_size(file_compressed_content))

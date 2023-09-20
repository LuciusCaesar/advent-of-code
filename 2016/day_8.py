"""Module to solve Day 8 of 2016 AoC"""
import re


class Digipass:
    def __init__(self):
        self._screen_width = 50
        self._screen_height = 6
        self.screen = [
            [0 for column in range(self._screen_width)]
            for line in range(self._screen_height)
        ]
        self.print_screen()

    def get_lit_pixels(self):
        return sum(sum(self.screen, []))

    def rect(self, columns: int, lines: int):
        for line in range(lines):
            for column in range(columns):
                self.screen[line][column] = 1

    def rotate_line(self, line: int, step: int):
        rotated_line = [
            self.screen[line][(column - step) % self._screen_width]
            for column in range(self._screen_width)
        ]

        self.screen[line] = rotated_line

    def rotate_column(self, column: int, step: int):
        rotated_column = [
            self.screen[(line - step) % self._screen_height][column]
            for line in range(self._screen_height)
        ]

        for line in range(self._screen_height):
            self.screen[line][column] = rotated_column[line]

    def print_screen(self):
        for line in range(self._screen_height):
            print(self.screen[line])
        print("")


def execute_instruction(digipass: Digipass, instruction: str):
    rect_instruction = re.search(r"rect (\d+)+x(\d+)", instruction)
    rotate_row_instruction = re.search(r"rotate row y=(\d+) by (\d+)", instruction)
    rotate_column_instruction = re.search(
        r"rotate column x=(\d+) by (\d+)", instruction
    )
    if rect_instruction:
        digipass.rect(int(rect_instruction.group(1)), int(rect_instruction.group(2)))
    elif rotate_row_instruction:
        digipass.rotate_line(
            int(rotate_row_instruction.group(1)), int(rotate_row_instruction.group(2))
        )
    elif rotate_column_instruction:
        digipass.rotate_column(
            int(rotate_column_instruction.group(1)),
            int(rotate_column_instruction.group(2)),
        )
    else:
        print("instruction not found")


with open("2016/day_8_input.txt", "r") as file:
    instructions = [line.strip() for line in file.readlines()]


digipass = Digipass()
print(digipass.get_lit_pixels())

for instruction in instructions:
    execute_instruction(digipass, instruction)
# digipass.rect(3, 2)
# digipass.print_screen()
# digipass.rotate_line(1, 2)
# digipass.print_screen()
# digipass.rotate_column(2, 7)
digipass.print_screen()
print(digipass.get_lit_pixels())

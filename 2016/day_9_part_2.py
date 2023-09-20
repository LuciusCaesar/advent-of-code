import re

REGEX = r"\((\d+)x(\d+)\)"

size = 0


class Reader:
    def __init__(self, multiplier: int = 1):
        self.multiplier = multiplier
        print("create reader")

    def read(self, string: str):
        print("read", string, "with multiplier", self.multiplier)
        # Split in two:
        match = re.match(REGEX, string)
        if not match:
            if not "(" in string:
                global size
                size += len(string) * self.multiplier
            elif "(" in string:
                index = string.index("(")
                first = string[:index]
                second = string[index:]
                Reader(self.multiplier).read(first)
                Reader(self.multiplier).read(second)
        elif match:
            index = match.end() + int(match.group(1))
            first = string[match.end() : index]
            second = string[index:]
            Reader(self.multiplier * int(match.group(2))).read(first)
            Reader(self.multiplier).read(second)
        else:
            print("do not know what to do here")

        return True


with open("2016/day_9_input.txt", "r") as file:
    file_contents = [line.strip() for line in file.readlines()]

file_compressed_content = file_contents[0]
reader = Reader().read(file_compressed_content)
print(size)

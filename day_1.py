"""
This is the first exercise of the 2016 Advent Calendar of Code
"""

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

RIGHT = "R"
LEFT = "L"

def manhattan_distance(position: tuple) -> int:
    """
    Calculates the Manhattan distance 
    of a position from the origin
    """
    return abs(position[0]) + abs(position[1])

class Robot():
    """The robot that follows the instructions of the elves"""
    def __init__(self, initial_direction) -> None:
        self.direction = initial_direction
        self.moves = [0,0,0,0]

    def apply_instruction(self, instruction:str) -> None:
        """
        Applies the instruction given in the file
        """
        robot.turn(instruction[0])
        robot.forward(int(instruction[1:]))

    def turn(self, sense:str) -> None:
        """Turn Right or Left"""
        if sense == RIGHT:
            self.direction = self.direction + 1 % 4
        if sense == LEFT:
            self.direction = self.direction - 1 % 4

    def forward(self, distance: int) -> None:
        """
        Once moved in the right direction, 
        the robot goes forward for a number of 
        steps representing the distance
        """
        self.moves[self.direction] += distance

    def get_position(self) -> tuple:
        """
        Position calculates the overal position on the grid 
        based on the total moves in all directions
        """
        return (self.moves[NORTH] - self.moves[SOUTH], self.moves[EAST] - self.moves[WEST])


# instructions = ["R2", "L3"]
instructions = ["R2", "R2", "R2"]
# instructions = ["R5", "L5", "R5", "R3"]
#TODO: read the sequence of instruction from a file

robot = Robot(NORTH)
for instruction in instructions:
    robot.apply_instruction(instruction)
    
coordinates = robot.get_position()
print(coordinates)
print(manhattan_distance(coordinates))
    
"""Day 10 AoC 2016"""
import re


class Chip:
    """Chip is defined by its value"""

    def __init__(self, value: int) -> None:
        self.value = value

    def get_value(self, value: int) -> int:
        return self.value


class ChipReceiver:
    """
    An abstract class used to implement the Observer of the Observer Pattern
    """

    def __init__(self) -> None:
        self.chips = []

    def receive_chip(self, chip: Chip) -> None:
        """The update function of the observer pattern"""
        self.chips.append(chip)


class ChipDispatcher:
    """
    An abstract class used to implement the Subject of the Observer Pattern
    """

    def subscribe_to_high(self, chip_receiver: ChipReceiver) -> None:
        """The attach function of the observer pattern"""
        self.high_chip_receiver = chip_receiver

    def subscribe_to_low(self, chip_receiver: ChipReceiver) -> None:
        """The attach function of the observer pattern"""
        self.low_chip_receiver = chip_receiver

    def dispatch_low(self, chip: Chip) -> None:
        """The notify function of the observer pattern"""
        self.low_chip_receiver.receive_chip(chip)

    def dispatch_high(self, chip: Chip) -> None:
        """The notify function of the observer pattern"""
        self.high_chip_receiver.receive_chip(chip)


class Bot(ChipReceiver, ChipDispatcher):
    def __init__(self, id: int) -> None:
        ChipReceiver.__init__(self)
        self.id = id

    def has_at_least_two_chips(self) -> bool:
        return len(self.chips) >= 2

    def dispatch(self):
        self.chips.sort(key=lambda x: x.value)
        print(
            "I am the bot "
            + str(self.id)
            + " dispatching "
            + str(self.chips[0].value)
            + " and "
            + str(self.chips[1].value)
        )
        self.dispatch_low(self.chips[0])
        self.dispatch_high(self.chips[1])
        self.chips = []


class OutputBin(ChipReceiver):
    def __init__(self, id: int) -> None:
        ChipReceiver.__init__(self)
        self.id = id


class Factory:
    """Factory is a collection of bots ant output bins"""

    def __init__(self) -> None:
        self.bots = {}
        self.output_bins = {}

    def retrieve_or_add_bot_by_id(self, bot_id: int) -> Bot:
        """
        Return a bot by its id
        Creates one if needed
        """
        if bot_id not in self.bots.keys():
            self.bots[bot_id] = Bot(bot_id)

        return self.bots[bot_id]

    def retrieve_or_add_output_bin_by_id(self, output_bin_id: int) -> OutputBin:
        """
        Returns an output bin by its id
        Creates one if needed
        """
        if output_bin_id not in self.output_bins.keys():
            self.output_bins[output_bin_id] = OutputBin(output_bin_id)

        return self.output_bins[output_bin_id]

    def get_bots_with_at_least_two_chips(self) -> list:
        return [bots for bots in self.bots.values() if bots.has_at_least_two_chips()]


# Script
with open("2016/day_10_input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

factory = Factory()
for line in lines:
    factory_instruction = re.match(
        r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)",
        line,
    )
    input_instruction = re.match(r"value (\d+) goes to bot (\d+)", line)

    if factory_instruction:
        # Treat factory instructions
        bot_id = int(factory_instruction.group(1))
        low_input_type = factory_instruction.group(2)
        low_destination_id = int(factory_instruction.group(3))
        high_input_type = factory_instruction.group(4)
        high_destination_id = int(factory_instruction.group(5))

        bot = factory.retrieve_or_add_bot_by_id(bot_id)
        if low_input_type == "bot":
            low_value_subscriber = factory.retrieve_or_add_bot_by_id(low_destination_id)
        elif low_input_type == "output":
            low_value_subscriber = factory.retrieve_or_add_output_bin_by_id(
                low_destination_id
            )
        else:
            raise ValueError()
        bot.subscribe_to_low(low_value_subscriber)

        if high_input_type == "bot":
            high_value_subscriber = factory.retrieve_or_add_bot_by_id(
                high_destination_id
            )
        elif high_input_type == "output":
            high_value_subscriber = factory.retrieve_or_add_output_bin_by_id(
                high_destination_id
            )
        else:
            raise ValueError()
        bot.subscribe_to_high(high_value_subscriber)

    elif input_instruction:
        # Treat input instructions
        bot_id = int(input_instruction.group(2))
        chip_value = int(input_instruction.group(1))
        factory.retrieve_or_add_bot_by_id(bot_id).chips.append(Chip(chip_value))

bots_with_two_chips = factory.get_bots_with_at_least_two_chips()

while len(bots_with_two_chips) >= 1:
    bot = bots_with_two_chips[0]
    bot.dispatch()
    bots_with_two_chips = factory.get_bots_with_at_least_two_chips()

print("done")

chip_value_0 = factory.retrieve_or_add_output_bin_by_id(0).chips[0].value
chip_value_1 = factory.retrieve_or_add_output_bin_by_id(1).chips[0].value
chip_value_2 = factory.retrieve_or_add_output_bin_by_id(2).chips[0].value

print(chip_value_0 * chip_value_1 * chip_value_2)

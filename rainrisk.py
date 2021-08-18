import sys


class Journey:
    @classmethod
    def from_instructions(cls, facing, instructions):
        journey = cls(facing)
        for instruction in instructions: journey.move(instruction)
        return journey

    def __init__(self, facing):
        self.facing = facing
        self.steps = []

    def move(self, instruction):
        command, argument = instruction[0], int(instruction[1:])
        method = {
            "L": self._turn,
            "R": self._turn,
        }.get(command, self._travel)
        method(command, argument)

    @property
    def manhattan_distance(self):
        horizontal = sum([step.horizontal for step in self.steps])
        vertical = sum([step.vertical for step in self.steps])
        return abs(horizontal) + abs(vertical)

    def _turn(self, command, argument):
        self.facing = Turn(command, argument, self.facing).now_facing

    def _travel(self, command, argument):
        self.steps.append(Step(self._direction(command), argument))

    def _direction(self, letter):
        if letter == "F":
            return self.facing
        return letter


class Step:
    def __init__(self, direction, distance):
        self.direction = direction
        self.distance = distance

    @property
    def horizontal(self):
        return self._distance_along_axis({"N": 0, "S": 0, "E": 1, "W": -1})

    @property
    def vertical(self):
        return self._distance_along_axis({"N": 1, "S": -1, "E": 0, "W": 0})

    def _distance_along_axis(self, signs):
        return self.distance * signs[self.direction]


class Turn:
    directions = ("N", "W", "S", "E")

    def __init__(self, direction, degrees, initially_facing):
        self.direction = direction
        self.degrees = degrees
        self.initial_index = self.directions.index(initially_facing)

    @property
    def now_facing(self):
        signs = {"L": 1, "R": -1}
        index_offset = signs[self.direction] * (self.degrees // 90)
        index = (self.initial_index + index_offset) % len(self.directions)
        return self.directions[index]


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        instructions = [line.rstrip() for line in f.readlines()]
    journey = Journey.from_instructions("E", instructions)
    print("Manhattan distance: %s" % journey.manhattan_distance)

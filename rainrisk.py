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
        default = lambda arg: self._travel(command, arg)
        action = {
            "L": lambda arg: self._turn(command, arg),
            "R": lambda arg: self._turn(command, arg),
            "F": lambda arg: self._travel(self.facing, arg)
        }.get(command, default)
        action(argument)

    @property
    def manhattan_distance(self):
        horizontal = sum([step.horizontal for step in self.steps])
        vertical = sum([step.vertical for step in self.steps])
        return abs(horizontal) + abs(vertical)

    def _turn(self, command, argument):
        self.facing = Turn(command, argument, self.facing).now_facing

    def _travel(self, command, argument):
        self.steps.append(Step(command, argument))


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
    directions = ("N", "E", "S", "W")

    def __init__(self, direction, degrees, initially_facing):
        self.direction = direction
        self.compass_points = degrees // 90
        self.initial_index = self.directions.index(initially_facing)

    @property
    def now_facing(self):
        return self.directions[self._direction_index()]

    def _direction_index(self):
        signs = {"L": -1, "R": 1}
        index_offset = signs[self.direction] * self.compass_points
        return (self.initial_index + index_offset) % len(self.directions)


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        instructions = [line.rstrip() for line in f.readlines()]
    journey = Journey.from_instructions("E", instructions)
    print("Manhattan distance: %s" % journey.manhattan_distance)

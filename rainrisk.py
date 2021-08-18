class Journey:
    def __init__(self):
        self.steps = []

    def travel(self, instruction):
        self.steps.append(Step(instruction[0], int(instruction[1:])))

    @property
    def manhattan_distance(self):
        horizontal = sum([step.horizontal for step in self.steps])
        vertical = sum([step.vertical for step in self.steps])
        return abs(horizontal) + abs(vertical)


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

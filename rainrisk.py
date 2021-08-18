class Journey:
    def __init__(self):
        self.steps = []

    def travel(self, instruction):
        self.steps.append(self._parse_instruction(instruction))

    @property
    def manhattan_distance(self):
        return sum([step[1] for step in self.steps])

    def _parse_instruction(self, instruction):
        direction = instruction[0]
        distance = int(instruction[1:])
        signs = {"N": 1, "S": -1}
        return (direction, distance * signs[direction])

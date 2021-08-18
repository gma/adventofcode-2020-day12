import unittest

import rainrisk


class JourneyTest(unittest.TestCase):
    def test_moving_north_updates_manhattan_distance(self):
        journey = rainrisk.Journey("E")
        journey.move("N2")
        self.assertEqual(2, journey.manhattan_distance)

    def test_moving_north_then_south_sets_correct_manhattan_distance(self):
        journey = rainrisk.Journey("E")
        journey.move("N1")
        journey.move("S1")
        self.assertEqual(0, journey.manhattan_distance)

    def test_moving_east_sets_manhattan_distance(self):
        journey = rainrisk.Journey("E")
        journey.move("E1")
        self.assertEqual(1, journey.manhattan_distance)

    def test_moving_east_then_west_sets_correct_manhattan_distance(self):
        journey = rainrisk.Journey("E")
        journey.move("E1")
        journey.move("W1")
        self.assertEqual(0, journey.manhattan_distance)

    def test_moving_west_sets_manhattan_distance(self):
        journey = rainrisk.Journey("E")
        journey.move("W1")
        self.assertEqual(1, journey.manhattan_distance)

    def test_moving_on_both_axes_sets_manhattan_distance(self):
        journey = rainrisk.Journey("E")
        journey.move("W1")
        journey.move("S3")
        journey.move("E2")
        self.assertEqual(4, journey.manhattan_distance)

    def test_moving_forwards_sets_manhattan_distance(self):
        journey = rainrisk.Journey("E")
        journey.move("F1")
        self.assertEqual(1, journey.manhattan_distance)

    def test_turning_left_and_right_changes_direction_faced(self):
        journey = rainrisk.Journey("N")
        journey.move("L90")
        self.assertEqual("W", journey.facing)
        journey.move("R180")
        self.assertEqual("E", journey.facing)


class TurnTest(unittest.TestCase):
    def test_turning_left_90_from_south_faces_east(self):
        turn = rainrisk.Turn("L", 90, "S")
        self.assertEqual("E", turn.now_facing)

    def test_turning_left_90_from_east_faces_north(self):
        turn = rainrisk.Turn("L", 90, "E")
        self.assertEqual("N", turn.now_facing)

    def test_turning_right_90_from_west_faces_south(self):
        turn = rainrisk.Turn("R", 90, "S")
        self.assertEqual("W", turn.now_facing)

    def test_turning_left_270_degrees_from_west_faces_south(self):
        turn = rainrisk.Turn("L", 270, "W")
        self.assertEqual("N", turn.now_facing)


if __name__ == "__main__":
    unittest.main()

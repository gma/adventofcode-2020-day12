import unittest

import rainrisk


class JourneyTest(unittest.TestCase):
    def test_moving_north_updates_manhattan_distance(self):
        journey = rainrisk.Journey("E")
        journey.travel("N2")
        self.assertEqual(2, journey.manhattan_distance)

    def test_moving_north_then_south_sets_correct_manhattan_distance(self):
        journey = rainrisk.Journey("E")
        journey.travel("N1")
        journey.travel("S1")
        self.assertEqual(0, journey.manhattan_distance)

    def test_moving_east_sets_manhattan_distance(self):
        journey = rainrisk.Journey("E")
        journey.travel("E1")
        self.assertEqual(1, journey.manhattan_distance)

    def test_moving_east_then_west_sets_correct_manhattan_distance(self):
        journey = rainrisk.Journey("E")
        journey.travel("E1")
        journey.travel("W1")
        self.assertEqual(0, journey.manhattan_distance)

    def test_moving_west_sets_manhattan_distance(self):
        journey = rainrisk.Journey("E")
        journey.travel("W1")
        self.assertEqual(1, journey.manhattan_distance)

    def test_moving_on_both_axes_sets_manhattan_distance(self):
        journey = rainrisk.Journey("E")
        journey.travel("W1")
        journey.travel("S3")
        journey.travel("E2")
        self.assertEqual(4, journey.manhattan_distance)

    def test_moving_forwards_sets_manhattan_distance(self):
        journey = rainrisk.Journey("E")
        journey.travel("F1")
        self.assertEqual(1, journey.manhattan_distance)


if __name__ == "__main__":
    unittest.main()

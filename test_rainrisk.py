import unittest

import rainrisk


class JourneyTest(unittest.TestCase):
    def test_moving_north_updates_manhattan_distance(self):
        journey = rainrisk.Journey()
        journey.travel("N2")
        self.assertEqual(2, journey.manhattan_distance)

    def test_moving_north_then_south_sets_correct_manhattan_distance(self):
        journey = rainrisk.Journey()
        journey.travel("N1")
        journey.travel("S1")
        self.assertEqual(0, journey.manhattan_distance)


if __name__ == "__main__":
    unittest.main()

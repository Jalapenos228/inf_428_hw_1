import math
import unittest


def time_to_cyclic(hour):
    radians = 2 * math.pi * (hour % 24) / 24
    return math.sin(radians), math.cos(radians)


def cyclic_time_difference(hour1, hour2):
    sin1, cos1 = time_to_cyclic(hour1)
    sin2, cos2 = time_to_cyclic(hour2)
    angle_diff = math.acos(sin1 * sin2 + cos1 * cos2)
    return 24 * angle_diff / (2 * math.pi)


class TestCyclicTimeFunctions(unittest.TestCase):

    def test_time_conversion(self):
        self.assertAlmostEqual(cyclic_time_difference(23, 1), 2, delta=0.1)
        self.assertAlmostEqual(cyclic_time_difference(1, 23), 2, delta=0.1)
        self.assertAlmostEqual(cyclic_time_difference(0, 12), 12, delta=0.1)
        self.assertAlmostEqual(cyclic_time_difference(6, 18), 12, delta=0.1)

    def test_same_time(self):
        self.assertAlmostEqual(cyclic_time_difference(10, 10), 0, delta=0.1)

    def test_halfway(self):
        self.assertAlmostEqual(cyclic_time_difference(0, 12), 12, delta=0.1)
        self.assertAlmostEqual(cyclic_time_difference(6, 18), 12, delta=0.1)


if __name__ == '__main__':
    unittest.main()

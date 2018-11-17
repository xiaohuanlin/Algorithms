import unittest
import random


def biased_random(p):
    '''
    :param p: the possibility of return 1
    :return: biased return 0 or 1
    '''
    indicator = random.uniform(0, 1)
    if indicator < p:
        return 1
    else:
        return 0


def unbiased_random(p):
    '''
    :param p: used for biased_random
    :return: uniform return 0 or 1
    '''

    indicator = random.randint(0, 1)
    if indicator == 1:
        return biased_random(p)
    else:
        return 1-biased_random(p)


class TestSolution(unittest.TestCase):

    def test_biased_random(self):
        examples = (
            (0.1, 10000, 1),
            (0.3, 50000, 2),
            (0.08, 1000000, 3),
        )
        for p, time, round_place in examples:
            self.assert_biased_random(p, time, round_place)

    def assert_biased_random(self, p, time, round_place):
        value = 0
        for _ in range(time):
            value += biased_random(p)
        self.assertAlmostEqual(value/time, p, delta=round_place)

    def test_case(self):
        examples = (
            (0.1, 10000, 1),
            (0.3, 50000, 2),
            (0.08, 1000000, 3),
        )
        for p, time, round_place in examples:
            self.assert_biased_random(p, time, round_place)

    def assert_function(self, p, time, round_place):
        value = 0
        for _ in range(time):
            value += biased_random(p)
        self.assertAlmostEqual(value/time, 0.5, delta=round_place)



unittest.main()

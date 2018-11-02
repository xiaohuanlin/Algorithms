'''

There are 1000 buckets, one and only one of them contains poison, the rest are filled with water. They all look the same. If a pig drinks that poison it will die within 15 minutes. What is the minimum amount of pigs you need to figure out which bucket contains the poison within one hour.

Answer this question, and write an algorithm for the follow-up general case.

Follow-up:

If there are n buckets and a pig drinking poison will die within m minutes, how many pigs (x) you need to figure out the "poison" bucket within p minutes? There is exact one bucket with poison.

'''
import unittest


class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        # pig can drink water efficient according like that
        # buckets  0   1   2   3
        # pig      __  a_  _b  ab
        # and use 2 pigs to test 4 buckets, just like use binary to represent the number
        # each pig have n round possibilities and alive, so the base is n+1, and will have number of pigs power
        # from math import log
        # answer = log(buckets, (minutesToTest / minutesToDie + 1))
        # if answer != int(answer):
        #     answer += 1
        # return int(answer)
        # ---------------
        bucket_one = minutesToTest / minutesToDie + 1
        result = 0
        while pow(bucket_one, result) < buckets:
            result += 1
        return result


class TestSolution(unittest.TestCase):

    def test_poorPigs(self):
        examples = (
            ((1000, 15, 60), 5),
            ((1, 1, 1), 0)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().poorPigs(*first), second, msg="first: {}; second: {}".format(first, second))

unittest.main()
'''

A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".

'''
import unittest


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # from itertools import combinations
        # hours = [1, 2, 4, 8]
        # minutes = [1, 2, 4, 8, 16, 32]
        # answer = set()
        # for h_times in range(num+1):
        #     m_times = num - h_times
        #     hours_list = list(sum(h) for h in combinations(hours, h_times))
        #     minutes_list = list(sum(m) for m in combinations(minutes, m_times))
        #
        #     for hour in hours_list:
        #         for minute in minutes_list:
        #             answer.add('{}:{:0>2d}'.format(hour, minute))
        # return list(answer)
        # -----------------------------
        return ['{}:{:0>2d}'.format(h, m) for h in range(12) for m in range(60) if bin(h).count('1') + bin(m).count('1') == num]


class TestSolution(unittest.TestCase):

    def test_readBinaryWatch(self):
        examples = (
            (1, ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]),
            # (2, ["0:03","0:05","0:06","0:09","0:10","0:12","0:17","0:18","0:20","0:24","0:33","0:34","0:36","0:40","0:48","1:01","1:02","1:04","1:08","1:16","1:32","2:01","2:02","2:04","2:08","2:16","2:32","3:00","4:01","4:02","4:04","4:08","4:16","4:32","5:00","6:00","8:01","8:02","8:04","8:08","8:16","8:32","9:00","10:00"]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().readBinaryWatch(first), second, msg="first: {}; second: {}".format(first, second))


unittest.main()
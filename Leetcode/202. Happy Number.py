'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''
import unittest

class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # n_list = {}
        # while n != 1:
        #     if n_list.get(n):
        #         return False
        #     n_list[n] = n
        #     sum_num = 0
        #     while n > 0:
        #         n, rem = divmod(n, 10)
        #         sum_num += rem**2
        #     n = sum_num
        # return True
        # -----------------------------------
        # generally speaking, this is the common linked-list, which we can get the next
        # number easily. And then, it is a encounter problem abstructly.
        def get_next(n):
            sum_num = 0
            while n > 0:
                n, rem = divmod(n, 10)
                sum_num += rem**2
            return sum_num
        
        slow, fast = n, n
        while True:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
            if slow == fast:
                break
        return slow == 1



class TestSolution(unittest.TestCase):

    def test_isHappy(self):
        examples = (
            # (19, True),
            # (18, False),
            (10, True),
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().isHappy(first), second)

unittest.main()
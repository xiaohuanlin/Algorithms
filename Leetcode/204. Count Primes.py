'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''
import unittest

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 0
        count = [1] * n
        count[0], count[1] = 0, 0
        for i in range(2, int(n**0.5) + 1):
            if count[i]:
                # because 2,3,...,i-1 has been wiped out, so just from i.
                for j in range(i * i, n, i):
                    count[j] = 0
        return sum(count)



class TestSolution(unittest.TestCase):

    def test_countPrimes(self):
        examples = (
            (10, 4),
            (2, 0)
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().countPrimes(first), second)

unittest.main()
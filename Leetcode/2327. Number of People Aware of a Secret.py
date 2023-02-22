'''
On day 1, one person discovers a secret.

You are given an integer delay, which means that each person will share the secret with a new person every day, starting from delay days after discovering the secret. You are also given an integer forget, which means that each person will forget the secret forget days after discovering it. A person cannot share the secret on the same day they forgot it, or on any day afterwards.

Given an integer n, return the number of people who know the secret at the end of day n. Since the answer may be very large, return it modulo 109 + 7.



Example 1:

Input: n = 6, delay = 2, forget = 4
Output: 5
Explanation:
Day 1: Suppose the first person is named A. (1 person)
Day 2: A is the only person who knows the secret. (1 person)
Day 3: A shares the secret with a new person, B. (2 people)
Day 4: A shares the secret with a new person, C. (3 people)
Day 5: A forgets the secret, and B shares the secret with a new person, D. (3 people)
Day 6: B shares the secret with E, and C shares the secret with F. (5 people)
Example 2:

Input: n = 4, delay = 1, forget = 3
Output: 6
Explanation:
Day 1: The first person is named A. (1 person)
Day 2: A shares the secret with B. (2 people)
Day 3: A and B share the secret with 2 new people, C and D. (4 people)
Day 4: A forgets the secret. B, C, and D share the secret with 3 new people. (6 people)


Constraints:

2 <= n <= 1000
1 <= delay < forget <= n
'''
import unittest

from typing import *


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = int(1e9+7)
        # calcalate the increase amount of everyday
        dp = [0 for _ in range(n)]
        dp[0] = 1
        for i in range(1, n):
            dp[i] = ((dp[i-1] if i != 1 else 0) - dp[i-forget] + dp[i-delay]) % mod
        return sum(dp[-forget:]) % mod


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((6,2,4),5),
            ((4,1,3),6),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().peopleAwareOfSecret(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

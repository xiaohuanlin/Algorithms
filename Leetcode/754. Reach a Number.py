'''

You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.
Example 2:
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.
Note:
target will be a non-zero integer in the range [-10^9, 10^9].

'''
import unittest


class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        # queue = [(0, 0)]
        # while queue:
        #     sum_value, n = queue.pop(0)
        #     if target == sum_value:
        #         return n
        #     queue.extend([(sum_value-(n+1), n+1), (sum_value+(n+1), n+1)])
        # ---------------------------------------------
        # the result of abs(target) and target is same
        target = abs(target)
        # assume that (n+1)*n / 2 = target
        n = int(((1+8*target)**0.5 - 1) / 2)
        if (n + 1) * n / 2 == target:
            return n
        # add 1 to n
        n += 1
        sum_n = (n + 1) * n / 2
        res = sum_n - target
        print(sum_n, target, n)
        if res % 2 == 0:
            return n
        elif (res + n + 1) % 2 == 0:
            # res is odd and if add n+1 then become even
            return n + 1
        else:
            # then n + 1 must is a even number, so n + 2 is a odd number, can be divide if add to res
            return n + 2


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (3, 2),
            (2, 3),
            (5, 5),
            (-1, 1),
            (-1000000000, 44723)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().reachNumber(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

'''

Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

'''
import unittest


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # from itertools import combinations
        # from math import sqrt
        # com = combinations(points, 3)
        # count = 0
        # for x1, x2, x3 in com:
        #     s1 = sqrt(sum((x-y)**2 for x, y in zip(x1, x2)))
        #     s2 = sqrt(sum((x - y) ** 2 for x, y in zip(x2, x3)))
        #     s3 = sqrt(sum((x - y) ** 2 for x, y in zip(x1, x3)))
        #     if s1 == s2 or s2 == s3 or s1 == s3:
        #         count += 2
        # return count
        # ---------------------
        # fix a point and then select 2 points in the same distance points, which is C2/N * 2
        from math import sqrt
        count = 0
        for fix_point in points:
            p_dict = {}
            for p in points:
                # store points and count the number
                distance = sqrt(sum((x - y) ** 2 for x, y in zip(fix_point, p)))
                p_dict[distance] = p_dict.setdefault(distance, 0) + 1

            for v in p_dict.values():
                count += v * (v - 1)
        return count


class TestSolution(unittest.TestCase):

    def test_numberOfBoomerangs(self):
        examples = (
            ([[0,0],[1,0],[2,0]], 2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numberOfBoomerangs(first), second, msg="first: {}; second: {}".format(first, second))

unittest.main()
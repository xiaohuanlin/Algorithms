'''
You are given an integer limit and a 2D array queries of size n x 2.

There are limit + 1 balls with distinct labels in the range [0, limit]. Initially, all balls are uncolored. For every query in queries that is of the form [x, y], you mark ball x with the color y. After each query, you need to find the number of distinct colors among the balls.

Return an array result of length n, where result[i] denotes the number of distinct colors after ith query.

Note that when answering a query, lack of a color will not be considered as a color.

 

Example 1:

Input: limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]

Output: [1,2,2,3]

Explanation:



After query 0, ball 1 has color 4.
After query 1, ball 1 has color 4, and ball 2 has color 5.
After query 2, ball 1 has color 3, and ball 2 has color 5.
After query 3, ball 1 has color 3, ball 2 has color 5, and ball 3 has color 4.
Example 2:

Input: limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]

Output: [1,2,2,3,4]

Explanation:



After query 0, ball 0 has color 1.
After query 1, ball 0 has color 1, and ball 1 has color 2.
After query 2, ball 0 has color 1, and balls 1 and 2 have color 2.
After query 3, ball 0 has color 1, balls 1 and 2 have color 2, and ball 3 has color 4.
After query 4, ball 0 has color 1, balls 1 and 2 have color 2, ball 3 has color 4, and ball 4 has color 5.
 

Constraints:

1 <= limit <= 109
1 <= n == queries.length <= 105
queries[i].length == 2
0 <= queries[i][0] <= limit
1 <= queries[i][1] <= 109
'''
from typing import *
import unittest


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # index => color
        maps_i = {}
        # color => counter
        maps_c = {}
        res = []
        for i, c in queries:
            if i in maps_i:
                maps_c[maps_i[i]] -= 1
                if maps_c[maps_i[i]] == 0:
                    del maps_c[maps_i[i]]
            maps_i[i] = c

            if c not in maps_c:
                maps_c[c] = 0
            maps_c[c] += 1

            res.append(len(maps_c))
        return res



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((4, [[1,4],[2,5],[1,3],[3,4]]), [1,2,2,3]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().queryResults(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
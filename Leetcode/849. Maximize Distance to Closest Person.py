'''

In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation:
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Note:

1 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.

'''
import unittest


class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        i = 0
        start = -1
        max_dis = 0
        while i < len(seats):
            if seats[i] == 0:
                if i == len(seats) - 1:
                    # print(i, start)
                    dis = i - start
                else:
                    i += 1
                    continue
            else:
                if start == -1:
                    # print(i, start)
                    dis = i
                    start = i
                else:
                    dis = (i - start) // 2
                    # print(mid, dis)
                    start = i
            # print(dis, max_dis)
            if dis > max_dis:
                max_dis = dis
            i += 1
        return max_dis


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([1,0,0,0,1,0,1], 2),
            ([1,0,0,0], 3),
            ([0,0,0,1], 3),
            ([0,1,0,0,0,0], 4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxDistToClosest(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

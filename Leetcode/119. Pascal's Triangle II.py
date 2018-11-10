'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
'''

import unittest

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        row = [1]
        n = 0
        ori_tmp = 1
        while n < rowIndex:
            for i in range(1,len(row)):
                tmp = row[i]
                row[i] = row[i] + ori_tmp
                ori_tmp = tmp
            row.append(1)

            n += 1
        return row

class TestSolution(unittest.TestCase):

    def test_getRow(self):
        examples = (
            (3,[1,3,3,1]),
            (0,[1]),
            (1,[1,1])
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().getRow(first), second)

unittest.main()
'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

import unittest

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        result = [[1],]
        row = [1]
        n = 1
        while n < numRows:
            new_row = [1]
            for i in range(1,len(row)):
                new_row.append(row[i] + row[i-1])
            new_row.append(1)
            result.append(new_row)

            row = new_row
            n += 1
        return result

class TestSolution(unittest.TestCase):

    def test_generate(self):
        examples = (

        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().generate(*first), second)

unittest.main()
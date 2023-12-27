'''
You are given a positive integer array grades which represents the grades of students in a university. You would like to enter all these students into a competition in ordered non-empty groups, such that the ordering meets the following conditions:

The sum of the grades of students in the ith group is less than the sum of the grades of students in the (i + 1)th group, for all groups (except the last).
The total number of students in the ith group is less than the total number of students in the (i + 1)th group, for all groups (except the last).
Return the maximum number of groups that can be formed.



Example 1:

Input: grades = [10,6,12,7,3,5]
Output: 3
Explanation: The following is a possible way to form 3 groups of students:
- 1st group has the students with grades = [12]. Sum of grades: 12. Student count: 1
- 2nd group has the students with grades = [6,7]. Sum of grades: 6 + 7 = 13. Student count: 2
- 3rd group has the students with grades = [10,3,5]. Sum of grades: 10 + 3 + 5 = 18. Student count: 3
It can be shown that it is not possible to form more than 3 groups.
Example 2:

Input: grades = [8,8]
Output: 1
Explanation: We can only form 1 group, since forming 2 groups would lead to an equal number of students in both groups.


Constraints:

1 <= grades.length <= 105
1 <= grades[i] <= 105
'''

from typing import *
import unittest


class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        start = 1
        end = 10**5
        candidate = None

        while start < end:
            middle = (start + end) // 2
            value = (middle + 1) * middle // 2
            if len(grades) < value:
                end = middle - 1
            else:
                candidate = middle
                start = middle + 1

        if (start + 1) * start // 2 <= len(grades):
            return start
        return candidate



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([10,6,12,7,3,5],),3),
            (([8,8],),1),
            (([2,31,41,31,36,46,33,45,47,8,31,6,12,12,15,35],),5),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maximumGroups(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

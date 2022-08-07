'''
There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
Output: 0.78333
Explanation: You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.
Example 2:

Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
Output: 0.53485
 

Constraints:

1 <= classes.length <= 105
classes[i].length == 2
1 <= passi <= totali <= 105
1 <= extraStudents <= 105
'''

from typing import *

import unittest

from heapq import heappush, heappop
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def calcu(top, bottom):
            return top/bottom - (top+1)/(bottom+1)
        
        heap = []
        for top, bottom in classes:
            heappush(heap, (calcu(top, bottom), top, bottom))
        
        for _ in range(extraStudents):
            _, top, bottom = heappop(heap)
            top += 1
            bottom += 1
            heappush(heap, (calcu(top, bottom), top, bottom))
            
        res = 0
        for _, top, bottom in heap:
            res += top / bottom
        return res / len(heap)
    
        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (([[2,4],[3,9],[4,5],[2,10]],4),0.5348484848484848),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxAverageRatio(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()


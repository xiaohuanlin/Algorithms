'''
You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array persons of size n, where persons[i] is the time that the ith person will arrive to see the flowers.

Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.

 

Example 1:


Input: flowers = [[1,6],[3,7],[9,12],[4,13]], persons = [2,3,7,11]
Output: [1,2,2,2]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.
Example 2:


Input: flowers = [[1,10],[3,3]], persons = [3,3,2]
Output: [2,2,1]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.
 

Constraints:

1 <= flowers.length <= 5 * 104
flowers[i].length == 2
1 <= starti <= endi <= 109
1 <= persons.length <= 5 * 104
1 <= persons[i] <= 109
'''
from typing import *
import unittest

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        num_list = []
        for s, e in flowers:
            num_list.append((s, 0, 0))
            num_list.append((e, 2, 0))
            
        for i, p in enumerate(persons):
            num_list.append((p, 1, i))
        
        num_list.sort()
        
        bloom = 0
        res = [0 for _ in range(len(persons))]
        for n, t, i in num_list:
            if t == 0:
                bloom += 1
            elif t == 1:
                res[i] = bloom
            else:
                bloom -= 1
        return res
        


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1,6],[3,7],[9,12],[4,13]], [2,3,7,11]), [1,2,2,2]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().fullBloomFlowers(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

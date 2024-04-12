'''
There is a test that has n types of questions. You are given an integer target and a 0-indexed 2D integer array types where types[i] = [counti, marksi] indicates that there are counti questions of the ith type, and each one of them is worth marksi points.

Return the number of ways you can earn exactly target points in the exam. Since the answer may be too large, return it modulo 109 + 7.

Note that questions of the same type are indistinguishable.

For example, if there are 3 questions of the same type, then solving the 1st and 2nd questions is the same as solving the 1st and 3rd questions, or the 2nd and 3rd questions.


Example 1:

Input: target = 6, types = [[6,1],[3,2],[2,3]]
Output: 7
Explanation: You can earn 6 points in one of the seven ways:
- Solve 6 questions of the 0th type: 1 + 1 + 1 + 1 + 1 + 1 = 6
- Solve 4 questions of the 0th type and 1 question of the 1st type: 1 + 1 + 1 + 1 + 2 = 6
- Solve 2 questions of the 0th type and 2 questions of the 1st type: 1 + 1 + 2 + 2 = 6
- Solve 3 questions of the 0th type and 1 question of the 2nd type: 1 + 1 + 1 + 3 = 6
- Solve 1 question of the 0th type, 1 question of the 1st type and 1 question of the 2nd type: 1 + 2 + 3 = 6
- Solve 3 questions of the 1st type: 2 + 2 + 2 = 6
- Solve 2 questions of the 2nd type: 3 + 3 = 6
Example 2:

Input: target = 5, types = [[50,1],[50,2],[50,5]]
Output: 4
Explanation: You can earn 5 points in one of the four ways:
- Solve 5 questions of the 0th type: 1 + 1 + 1 + 1 + 1 = 5
- Solve 3 questions of the 0th type and 1 question of the 1st type: 1 + 1 + 1 + 2 = 5
- Solve 1 questions of the 0th type and 2 questions of the 1st type: 1 + 2 + 2 = 5
- Solve 1 question of the 2nd type: 5
Example 3:

Input: target = 18, types = [[6,1],[3,2],[2,3]]
Output: 1
Explanation: You can only earn 18 points by answering all questions.


Constraints:

1 <= target <= 1000
n == types.length
1 <= n <= 50
types[i].length == 2
1 <= counti, marksi <= 50
'''
import unittest

from typing import *


from collections import defaultdict

class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        maps = defaultdict(int)
        res = 0
        maps[0] = 1
        con = int(1e9 + 7)
        for count, mark in types:
            old_map = {k: v for k, v in maps.items()}
            for i in range(1, count + 1):
                pre_target = target - (i * mark)
                if pre_target in old_map:
                    res += old_map[pre_target]
                    res %= con
                for k, v in old_map.items():
                    key = k + i * mark
                    if key < target:
                        maps[key] += old_map[k]
                        maps[key] %= con
        return res



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((6, [[6,1],[3,2],[2,3]]), 7),
            ((500, [[6,1],[49,2],[33,3],[26,4],[28,5],[45,6],[4,7],[23,8],[46,9],[39,10],[12,11],[28,12],[37,13],[18,14],[10,15],[27,16],[26,17],[10,18],[34,19],[11,20],[35,21],[5,22],[47,23],[19,24],[15,25],[27,26],[50,27],[3,28],[24,29],[18,30],[49,31],[32,32],[18,33],[5,34],[34,35]],), 342808744),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().waysToReachTarget(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

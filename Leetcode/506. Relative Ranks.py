'''

Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.

'''
import unittest


class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        score_rank = {n:str(i+1) for i, n in enumerate(sorted(nums, reverse=True))}
        result = []
        for n in nums:
            if score_rank[n] == '1':
                result.append('Gold Medal')
            elif score_rank[n] == '2':
                result.append('Silver Medal')
            elif score_rank[n] == '3':
                result.append('Bronze Medal')
            else:
                result.append(score_rank[n])
        return result


class TestSolution(unittest.TestCase):

    def test_findRelativeRanks(self):
        examples = (
            ([5, 4, 3, 2, 1], ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findRelativeRanks(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
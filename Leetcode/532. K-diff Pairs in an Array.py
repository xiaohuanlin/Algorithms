'''

Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].

'''
import unittest


class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # from collections import defaultdict
        # if k < 0:
        #     return 0
        # result = defaultdict(set)
        # for i, n in enumerate(nums):
        #     min_v = n - k
        #     max_v = n + k
        #     result[min_v].add(i)
        #     result[max_v].add(i)
        #
        # print(result)
        # result_list = set()
        # for i, n in enumerate(nums):
        #     if n in result:
        #         for index in result[n]:
        #             if index != i:
        #                 result_list.add((min(nums[index], n), max(nums[index], n)))
        # return len(result_list)
        # -----------------------------
        from collections import Counter
        if k < 0:
            return 0
        if k > 0:
            return len(set(nums) & set(n+k for n in nums))
        else:
            return sum(v > 1 for v in Counter(nums).values())


class TestSolution(unittest.TestCase):

    def test_findPairs(self):
        examples = (
            (([3, 1, 4, 1, 5], 2), 2),
            (([1, 2, 3, 4, 5], 1), 4),
            (([1, 3, 1, 5, 4], 0), 1),
            (([1, 3, 1, 5, 4], 10), 0),
            (([], 1), 0),
            (([1,2,3,4,5], -1), 0),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findPairs(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
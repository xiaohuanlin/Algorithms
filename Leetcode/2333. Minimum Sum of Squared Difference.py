'''
You are given two positive 0-indexed integer arrays nums1 and nums2, both of length n.

The sum of squared difference of arrays nums1 and nums2 is defined as the sum of (nums1[i] - nums2[i])2 for each 0 <= i < n.

You are also given two positive integers k1 and k2. You can modify any of the elements of nums1 by +1 or -1 at most k1 times. Similarly, you can modify any of the elements of nums2 by +1 or -1 at most k2 times.

Return the minimum sum of squared difference after modifying array nums1 at most k1 times and modifying array nums2 at most k2 times.

Note: You are allowed to modify the array elements to become negative integers.

 

Example 1:

Input: nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0
Output: 579
Explanation: The elements in nums1 and nums2 cannot be modified because k1 = 0 and k2 = 0. 
The sum of square difference will be: (1 - 2)2 + (2 - 10)2 + (3 - 20)2 + (4 - 19)2 = 579.
Example 2:

Input: nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1
Output: 43
Explanation: One way to obtain the minimum sum of square difference is: 
- Increase nums1[0] once.
- Increase nums2[2] once.
The minimum of the sum of square difference will be: 
(2 - 5)2 + (4 - 8)2 + (10 - 7)2 + (12 - 9)2 = 43.
Note that, there are other ways to obtain the minimum of the sum of square difference, but there is no way to obtain a sum smaller than 43.
 

Constraints:

n == nums1.length == nums2.length
1 <= n <= 105
0 <= nums1[i], nums2[i] <= 105
0 <= k1, k2 <= 109
'''
from typing import *
import unittest

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        h = []
        for i in range(len(nums1)):
            h.append(abs(nums1[i] - nums2[i]))
        
        cnt = k1 + k2
        def is_good(n):
            res = 0
            for i in h:
                if i > n:
                    res += (i - n)
            return res <= cnt

        start = 0
        end = max(h)
        while start < end:
            middle = start + (end - start) // 2
            if is_good(middle):
                end = middle
            else:
                start = middle + 1
        
        for i in range(len(h)):
            delta = max(0, h[i] - start)
            h[i] -= delta
            cnt -= delta

        res = 0
        for i in range(len(h)):
            if cnt > 0 and h[i] == start and h[i] > 0:
                cnt -= 1
                h[i] -= 1
            res += h[i] ** 2
        return res

                    

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            # (([1,4,10,12],[5,8,6,9],1,1),43),
            # (([1,4,10,12],[5,8,6,9],10,5),0),
            (([10,10,10,11,5],[1,0,6,6,1],11,27),0),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minSumSquareDiff(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

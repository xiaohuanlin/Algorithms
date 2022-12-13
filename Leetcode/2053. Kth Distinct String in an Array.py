'''
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.

 

Example 1:

Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned. 
Example 2:

Input: arr = ["aaa","aa","a"], k = 1
Output: "aaa"
Explanation:
All strings in arr are distinct, so the 1st string "aaa" is returned.
Example 3:

Input: arr = ["a","b","a"], k = 3
Output: ""
Explanation:
The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".
 

Constraints:

1 <= k <= arr.length <= 1000
1 <= arr[i].length <= 5
arr[i] consists of lowercase English letters.
'''
from typing import *

import unittest

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        locations = {}
        cnt = 0
        for i in range(len(arr)):
            if arr[i] not in locations:
                locations[arr[i]] = i
            else:
                locations[arr[i]] = -1
        
        res = []
        for key, value in locations.items():
            if value != -1:
                res.append((value, key))
        res.sort()
        return "" if (len(res) < k) else res[k-1][1]
        

        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((["d","b","c","b","c","a"], 2), 'a'),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().kthDistinct(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()



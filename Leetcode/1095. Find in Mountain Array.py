'''
(This problem is an interactive problem.)

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

Example 1:

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
Example 2:

Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.
 

Constraints:

3 <= mountain_arr.length() <= 104
0 <= target <= 109
0 <= mountain_arr.get(index) <= 109
'''
import unittest
from bisect import bisect

class MountainArray:
   def get(self, index: int) -> int:
       pass
    
   def length(self) -> int:
       pass

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # find the montain
        start = 0
        end = mountain_arr.length() - 1
        while start < end:
            middle = (start + end) // 2
            middle_prev = middle - 1
            middle_next = middle + 1
            middle_v = mountain_arr.get(middle)
            if middle_v < mountain_arr.get(middle_next):
                start = middle_next
            elif middle_v > mountain_arr.get(middle_prev):
                # montain
                start = middle
                break
            else:
                end = middle - 1
        mountain = mountain_arr.get(start)
                    
        left = mountain_arr.get(0)
        right = mountain_arr.get(mountain_arr.length() - 1)
        if target < min(left, right) or target > mountain:
            return -1
        elif target == left:
            return 0
        elif target == mountain:
            return start
        else:
            # find in left
            ans_left = self.find(target, mountain_arr, 1, start - 1, True)
            if ans_left != -1:
                return ans_left
            # find in right
            ans_right = self.find(target, mountain_arr, start + 1, mountain_arr.length() - 1, False)
            if ans_right != -1:
                return ans_right
            return -1

    def find(self, target: int, mountain_arr: 'MountainArray', start, end, asc):
        if start > end:
            return -1

        while start < end:
            middle = (start + end) // 2
            middle_v = mountain_arr.get(middle)
            if middle_v < target:
                if asc:
                    start = middle + 1
                else:
                    end = middle - 1
            elif middle_v == target:
                return middle
            else:
                if asc:
                    end = middle - 1
                else:
                    start = middle + 1
        return start if mountain_arr.get(start) == target else -1

                

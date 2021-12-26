import java.util.*;

// Given an integer array nums and two integers firstLen and secondLen, return the maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.

// The array with length firstLen could occur before or after the array with length secondLen, but they have to be non-overlapping.

// A subarray is a contiguous part of an array.

 

// Example 1:

// Input: nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
// Output: 20
// Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.
// Example 2:

// Input: nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
// Output: 29
// Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.
// Example 3:

// Input: nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
// Output: 31
// Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.
 

// Constraints:

// 1 <= firstLen, secondLen <= 1000
// 2 <= firstLen + secondLen <= 1000
// firstLen + secondLen <= nums.length <= 1000
// 0 <= nums[i] <= 1000

class Solution1031 {
    public int maxSumTwoNoOverlap(int[] nums, int firstLen, int secondLen) {
        return Math.max(innerMaxSumTwoNoOverlap(nums, firstLen, secondLen), innerMaxSumTwoNoOverlap(nums, secondLen, firstLen));
    }

    public int innerMaxSumTwoNoOverlap(int[] nums, int firstLen, int secondLen) {
        int[] firstEndArray = new int[nums.length];
        int[] firstMaxArray = new int[nums.length];
        int[] secondStartArray = new int[nums.length];
        int[] secondMaxArray = new int[nums.length];

        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            // find the arrays which ends with length equal firstLen
            sum += nums[i];
            if (i - firstLen >= 0) {
                sum -= nums[i - firstLen];
            }
            firstEndArray[i] = sum;
            if (i - 1 >= 0) {
                firstMaxArray[i] = Math.max(firstMaxArray[i - 1], sum);
            } else {
                firstMaxArray[i] = sum;
            }
        }

        sum = 0;
        for (int i = nums.length - 1; i >= 0; i--) {
            // find the arrays which starts with length equal secondLen
            sum += nums[i];
            if (i + secondLen < nums.length) {
                sum -= nums[i + secondLen];
            }
            secondStartArray[i] = sum;
            if (i + 1 < nums.length) {
                secondMaxArray[i] = Math.max(secondMaxArray[i + 1], sum);
            } else {
                secondMaxArray[i] = sum;
            }
        }

        int max = 0;
        for (int i = firstLen - 1; i < nums.length - 1; i++) {
            max = Math.max(max, firstEndArray[i] + secondMaxArray[i + 1]);
        }
        return max;
    }
}

class Driver1031 {
    public static void main(String[] args) {
        int[] nums = {1,0,1};
        int firstLen = 1;
        int secondLen = 1;
        System.out.println((new Solution1031()).maxSumTwoNoOverlap(nums, firstLen, secondLen));
    }
}
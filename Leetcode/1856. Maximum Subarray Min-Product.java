import java.util.*;

// The min-product of an array is equal to the minimum value in the array multiplied by the array's sum.

// For example, the array [3,2,5] (minimum value is 2) has a min-product of 2 * (3+2+5) = 2 * 10 = 20.
// Given an array of integers nums, return the maximum min-product of any non-empty subarray of nums. Since the answer may be large, return it modulo 109 + 7.

// Note that the min-product should be maximized before performing the modulo operation. Testcases are generated such that the maximum min-product without modulo will fit in a 64-bit signed integer.

// A subarray is a contiguous part of an array.

 

// Example 1:

// Input: nums = [1,2,3,2]
// Output: 14
// Explanation: The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2).
// 2 * (2+3+2) = 2 * 7 = 14.
// Example 2:

// Input: nums = [2,3,3,1,2]
// Output: 18
// Explanation: The maximum min-product is achieved with the subarray [3,3] (minimum value is 3).
// 3 * (3+3) = 3 * 6 = 18.
// Example 3:

// Input: nums = [3,1,5,6,4,2]
// Output: 60
// Explanation: The maximum min-product is achieved with the subarray [5,6,4] (minimum value is 4).
// 4 * (5+6+4) = 4 * 15 = 60.
 

// Constraints:

// 1 <= nums.length <= 105
// 1 <= nums[i] <= 10^7

class Solution1856 {
    public int maxSumMinProduct(int[] nums) {
        int[] prevMin = new int[nums.length];
        int[] nextMin = new int[nums.length];
        long[] prefixSum = new long[nums.length];

        prefixSum[0] = nums[0];
        for (int i = 0; i < nums.length - 1; i++) {
            prefixSum[i + 1] = prefixSum[i] + nums[i + 1];
        }

        Stack<Integer> s = new Stack<>();
        for (int i = nums.length - 1; i >= 0; i--) {
            while (!s.empty() && nums[s.peek()] >= nums[i]) {
                s.pop();
            }
            nextMin[i] = s.empty() ? nums.length: s.peek();
            s.add(i);
        }

        s.clear();
        for (int i = 0; i < nums.length; i++) {
            while (!s.empty() && nums[s.peek()] >= nums[i]) {
                s.pop();
            }
            prevMin[i] = s.empty() ? -1: s.peek();
            s.add(i);
        }

        long max = 0;
        for (int i = 0; i < nums.length; i++) {
            long sum = prefixSum[nextMin[i] - 1] - (prevMin[i] == -1 ? 0: prefixSum[prevMin[i]]);
            max = Math.max(sum * nums[i], max);
        }
        return (int)(max % (1_000_000_000 + 7));
    }
}

class Driver1856 {
    public static void main(String[] args) {
        int[] nums = {1,2,3,2};
        System.out.println((new Solution1856()).maxSumMinProduct(nums));
    }
}
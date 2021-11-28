import java.util.*;

// Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

// A subarray is a contiguous part of an array.

 

// Example 1:

// Input: nums = [4,5,0,-2,-3,1], k = 5
// Output: 7
// Explanation: There are 7 subarrays with a sum divisible by k = 5:
// [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
// Example 2:

// Input: nums = [5], k = 9
// Output: 0
 

// Constraints:

// 1 <= nums.length <= 3 * 10^4
// -10^4 <= nums[i] <= 10^4
// 2 <= k <= 10^4

class Solution1498 {
    public int numSubseq(int[] nums, int target) {
        Arrays.sort(nums);
        System.out.println(Arrays.toString(nums));

        int[] twoPower = new int[nums.length];
        twoPower[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            twoPower[i] = (twoPower[i - 1] * 2) % (1_000_000_007);
        }

        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            int max = target - nums[i];
            int pos = upperBound(nums, i, nums.length, max) - 1;
            if (pos < i) {
                continue;
            }
            res = (res + twoPower[pos - i]) % (1_000_000_007);
        }
        return res;
    }

    public int upperBound(int[] nums, int start, int end, int target) {
        while (start < end) {
            int middle = (end - start) / 2 + start;
            if (nums[middle] <= target) {
                start = middle + 1;
            } else if (nums[middle] > target) {
                end = middle;
            }
        }
        return start < nums.length && nums[start] == target ? start + 1: start;
    }
}

class Driver1498 {
    public static void main(String[] args) {
        Solution1498 solution = new Solution1498();

        int[] nums = {7,10,7,3,7,5,4};
        int target = 12;
        System.out.println(solution.numSubseq(nums, target));
    }
}
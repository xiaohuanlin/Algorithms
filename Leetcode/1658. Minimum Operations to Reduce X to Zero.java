import java.util.*;

// You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

// Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

 

// Example 1:

// Input: nums = [1,1,4,2,3], x = 5
// Output: 2
// Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
// Example 2:

// Input: nums = [5,6,7,8,9], x = 4
// Output: -1
// Example 3:

// Input: nums = [3,2,20,1,1,3], x = 10
// Output: 5
// Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
 

// Constraints:

// 1 <= nums.length <= 105
// 1 <= nums[i] <= 104
// 1 <= x <= 109

class Solution1658 {
    public int minOperations(int[] nums, int x) {
        int left = 0;
        int right = 0;
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
        }

        int target = sum - x;
        if (target < 0) {
            return -1;
        }
        sum = 0;
        int res = Integer.MAX_VALUE;
        while (right < nums.length) {
            while (right < nums.length && sum < target) {
                sum += nums[right++];
            }

            while (left < nums.length && sum > target) {
                sum -= nums[left++];
            }

            if (sum == target) {
                res = Math.min(res, nums.length - (right - left));

                if (right < nums.length) {
                    sum += nums[right++];
                }
            }
        }
        if (sum == target) {
            res = Math.min(res, nums.length - (right - left));
        }

        return res == Integer.MAX_VALUE ? -1 : res;
    }
}

class Driver1658 {
    public static void main(String[] args) {
        int[] nums = {1,1};
        int x = 3;
        System.out.println((new Solution1658()).minOperations(nums, x));
    }
}
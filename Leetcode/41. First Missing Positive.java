import java.util.*;

// Given an unsorted integer array nums, return the smallest missing positive integer.

// You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

// Example 1:

// Input: nums = [1,2,0]
// Output: 3
// Example 2:

// Input: nums = [3,4,-1,1]
// Output: 2
// Example 3:

// Input: nums = [7,8,9,11,12]
// Output: 1
 

// Constraints:

// 1 <= nums.length <= 5 * 10^5
// -2^31 <= nums[i] <= 2^31 - 1

class Solution41 {
    public int firstMissingPositive(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int next = nums[i] - 1;
            while (next != i && next >= 0 && next < nums.length && nums[next] != nums[i]) {
                // swap
                nums[i] = nums[next];
                nums[next] = next + 1;

                next = nums[i] - 1;
            }
        }

        for (int i = 0; i < nums.length; i++) {
            if (i + 1 != nums[i]) {
                return i + 1;
            }
        }

        return nums.length + 1;
    }
}

class Driver41 {
    public static void main(String[] args) {
        int[] nums = {1,2,2};
        System.out.println(new Solution41().firstMissingPositive(nums));
    }
}
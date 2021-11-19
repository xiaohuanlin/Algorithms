import java.util.*;

// You are given a 0-indexed integer array nums. For each index i (1 <= i <= nums.length - 2) the beauty of nums[i] equals:

// 2, if nums[j] < nums[i] < nums[k], for all 0 <= j < i and for all i < k <= nums.length - 1.
// 1, if nums[i - 1] < nums[i] < nums[i + 1], and the previous condition is not satisfied.
// 0, if none of the previous conditions holds.
// Return the sum of beauty of all nums[i] where 1 <= i <= nums.length - 2.

 

// Example 1:

// Input: nums = [1,2,3]
// Output: 2
// Explanation: For each index i in the range 1 <= i <= 1:
// - The beauty of nums[1] equals 2.
// Example 2:

// Input: nums = [2,4,6,4]
// Output: 1
// Explanation: For each index i in the range 1 <= i <= 2:
// - The beauty of nums[1] equals 1.
// - The beauty of nums[2] equals 0.
// Example 3:

// Input: nums = [3,2,1]
// Output: 0
// Explanation: For each index i in the range 1 <= i <= 1:
// - The beauty of nums[1] equals 0.
 

// Constraints:

// 3 <= nums.length <= 105
// 1 <= nums[i] <= 105

class Solution2012 {
    public int sumOfBeauties(int[] nums) {
        int[] prevGreater = new int[nums.length];
        int[] nextLesser = new int[nums.length];
        Stack<Integer> candidates = new Stack<>();

        for (int i = nums.length - 1; i >= 0; i--) {
            while (!candidates.empty() && candidates.peek() > nums[i]) {
                candidates.pop();
            }
            nextLesser[i] = candidates.empty() ? -1 : candidates.peek();
            candidates.push(nums[i]);
        }

        for (int i = 0; i < nums.length; i++) {
            while (!candidates.empty() && candidates.peek() < nums[i]) {
                candidates.pop();
            }
            prevGreater[i] = candidates.empty() ? -1 : candidates.peek();
            candidates.push(nums[i]);
        }

        int count = 0;
        for (int i = 1; i < nums.length - 1; i++) {
            if (prevGreater[i] == -1 && nextLesser[i] == -1) {
                count += 2;
            } else if (nums[i - 1] < nums[i] && nums[i] < nums[i + 1]) {
                count++;
            }
        }
        return count;
    }
}

class Driver2012 {
    public static void main(String[] args) {
        Solution2012 solution = new Solution2012();

        int[] nums = {1,2,3,2,1};
        System.out.println(solution.sumOfBeauties(nums));
    }
}
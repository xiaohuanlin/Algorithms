import java.util.*;

// You are given an integer array nums that is sorted in non-decreasing order.

// Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:

// Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
// All subsequences have a length of 3 or more.
// Return true if you can split nums according to the above conditions, or false otherwise.

// A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).

 

// Example 1:

// Input: nums = [1,2,3,3,4,5]
// Output: true
// Explanation: nums can be split into the following subsequences:
// [1,2,3,3,4,5] --> 1, 2, 3
// [1,2,3,3,4,5] --> 3, 4, 5
// Example 2:

// Input: nums = [1,2,3,3,4,4,5,5]
// Output: true
// Explanation: nums can be split into the following subsequences:
// [1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
// [1,2,3,3,4,4,5,5] --> 3, 4, 5
// Example 3:

// Input: nums = [1,2,3,4,4,5]
// Output: false
// Explanation: It is impossible to split nums into consecutive increasing subsequences of length 3 or more.
 

// Constraints:

// 1 <= nums.length <= 10^4
// -1000 <= nums[i] <= 1000
// nums is sorted in non-decreasing order.


class Solution659 {

    public boolean isPossible(int[] nums) {
        Map<Integer, Integer> exists = new HashMap<>();
        Map<Integer, Integer> needs = new HashMap<>();

        for (int v: nums) {
            exists.put(v, exists.getOrDefault(v, 0) + 1);
        }

        for (int v: nums) {
            if (exists.get(v) == 0) {
                continue;
            }

            if (needs.getOrDefault(v, 0) > 0) {
                needs.put(v, needs.get(v) - 1);
                needs.put(v + 1, needs.getOrDefault(v + 1, 0) + 1);
            } else if (exists.getOrDefault(v + 1, 0) > 0 && exists.getOrDefault(v + 2, 0) > 0) {
                exists.put(v + 1, exists.get(v + 1) - 1);
                exists.put(v + 2, exists.get(v + 2) - 1);
                needs.put(v + 3, needs.getOrDefault(v + 3, 0) + 1);
            } else {
                return false;
            }
            exists.put(v, exists.get(v) - 1);
        }
        return true;
    }
}

class Driver659 {
    public static void main(String[] args) {
        Solution659 solution = new Solution659();

        int[] nums = {1,2,3,3,4,4,5,5};
        System.out.println(solution.isPossible(nums));
    }
}
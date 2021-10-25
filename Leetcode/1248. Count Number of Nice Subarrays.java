import java.util.*;

// Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

// Return the number of nice sub-arrays.

 

// Example 1:

// Input: nums = [1,1,2,1,1], k = 3
// Output: 2
// Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
// Example 2:

// Input: nums = [2,4,6], k = 1
// Output: 0
// Explanation: There is no odd numbers in the array.
// Example 3:

// Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
// Output: 16
 

// Constraints:

// 1 <= nums.length <= 50000
// 1 <= nums[i] <= 10^5
// 1 <= k <= nums.length

class Solution1248 {
    public int numberOfSubarrays(int[] nums, int k) {
        List<Integer> oddPos = new ArrayList<>();
        oddPos.add(-1);
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] % 2 == 1) {
                oddPos.add(i);
            }
        }
        oddPos.add(nums.length);

        if ((oddPos.size() - 2) < k) {
            return 0;
        }

        int res = 0;
        for (int i = 1; i + k < oddPos.size(); i++) {
            res += (oddPos.get(i) - oddPos.get(i - 1)) * (oddPos.get(i + k) - oddPos.get(i + k - 1));
        }
        return res;
    }
}

class Driver1248 {
    public static void main(String[] args) {
        Solution1248 solution = new Solution1248();

        int[] nums = {1,1,2,1,1};
        int k = 3;
        System.out.println(solution.numberOfSubarrays(nums, k));
    }
}
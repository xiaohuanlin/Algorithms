import java.util.*;

// You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

// Return the maximum score you can get by erasing exactly one subarray.

// An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

 

// Example 1:

// Input: nums = [4,2,4,5,6]
// Output: 17
// Explanation: The optimal subarray here is [2,4,5,6].
// Example 2:

// Input: nums = [5,2,1,2,5,2,1,2,5]
// Output: 8
// Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
 

// Constraints:

// 1 <= nums.length <= 105
// 1 <= nums[i] <= 104

class Solution1695 {
    public int maximumUniqueSubarray(int[] nums) {
        int left = 0;
        int right = 0;
        Set<Integer> counts = new HashSet<>();

        int max = 0;
        int sum = 0;
        // init
        while (right < nums.length) {

            while (right < nums.length && !counts.contains(nums[right])) {
                counts.add(nums[right]);
                sum += nums[right];
                right++;
            }
            max = Math.max(max, sum);

            // shift left
            counts.remove(nums[left]);
            sum -= nums[left];
            left++;
        }
        return max;
    }
}

class Driver1695 {
    public static void main(String[] args) {
        int[] nums = {5,2,1,2,5,2,1,2,5};
        System.out.println((new Solution1695()).maximumUniqueSubarray(nums));
    }
}
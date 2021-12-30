import java.util.*;

// Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers.

// Return true if it is possible. Otherwise, return false.

 

// Example 1:

// Input: nums = [1,2,3,3,4,4,5,6], k = 4
// Output: true
// Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
// Example 2:

// Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
// Output: true
// Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
// Example 3:

// Input: nums = [1,2,3,4], k = 3
// Output: false
// Explanation: Each array should be divided in subarrays of size 3.
 

// Constraints:

// 1 <= k <= nums.length <= 105
// 1 <= nums[i] <= 109
 

// Note: This question is the same as 846: https://leetcode.com/problems/hand-of-straights/

class Solution1296 {
    public boolean isPossibleDivide(int[] nums, int k) {
        Arrays.sort(nums);
        Map<Integer, Queue<Integer>> maps = new HashMap<>();

        for (int num: nums) {
            if (maps.containsKey(num) && maps.get(num).size() > 0) {
                int nextK = maps.get(num).poll();
                if (nextK == 1) {
                    continue;
                }

                Queue<Integer> list;
                if (!maps.containsKey(num + 1)) {
                    list = new LinkedList<>();
                    maps.put(num + 1, list);
                } else {
                    list = maps.get(num + 1);
                }
                list.offer(nextK - 1);
            } else {
                if (k == 1) {
                    continue;
                }

                Queue<Integer> list;
                if (!maps.containsKey(num + 1)) {
                    list = new LinkedList<>();
                    maps.put(num + 1, list);
                } else {
                    list = maps.get(num + 1);
                }

                list.offer(k - 1);
            }
        }

        for (Map.Entry<Integer, Queue<Integer>> entry: maps.entrySet()) {
            if (entry.getValue().size() > 0) {
                return false;
            }
        }
        return true;
    }
}

class Driver1296 {
    public static void main(String[] args) {
        int[] nums = {3,3,2,2,1,1};
        int k = 3;
        System.out.println((new Solution1296()).isPossibleDivide(nums, k));
    }
}
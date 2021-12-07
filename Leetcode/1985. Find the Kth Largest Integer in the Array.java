import java.util.*;

// You are given an array of strings nums and an integer k. Each string in nums represents an integer without leading zeros.

// Return the string that represents the kth largest integer in nums.

// Note: Duplicate numbers should be counted distinctly. For example, if nums is ["1","2","2"], "2" is the first largest integer, "2" is the second-largest integer, and "1" is the third-largest integer.

 

// Example 1:

// Input: nums = ["3","6","7","10"], k = 4
// Output: "3"
// Explanation:
// The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
// The 4th largest integer in nums is "3".
// Example 2:

// Input: nums = ["2","21","12","1"], k = 3
// Output: "2"
// Explanation:
// The numbers in nums sorted in non-decreasing order are ["1","2","12","21"].
// The 3rd largest integer in nums is "2".
// Example 3:

// Input: nums = ["0","0"], k = 2
// Output: "0"
// Explanation:
// The numbers in nums sorted in non-decreasing order are ["0","0"].
// The 2nd largest integer in nums is "0".
 

// Constraints:

// 1 <= k <= nums.length <= 104
// 1 <= nums[i].length <= 100
// nums[i] consists of only digits.
// nums[i] will not have any leading zeros.

class Solution1985 {
    public String kthLargestNumber(String[] nums, int k) {
        PriorityQueue<String> pq = new PriorityQueue<>(new Comparator<String>() {

            @Override
            public int compare(String arg0, String arg1) {
                // TODO Auto-generated method stub
                int arg0Length = arg0.length();
                int arg1Length = arg1.length();
                if (arg0Length != arg1Length) {
                    return Integer.compare(arg1Length, arg0Length);
                }
                
                int i = 0;
                int length = Math.min(arg0Length, arg1Length);
                while (i < length) {
                    if (arg0.charAt(i) != arg1.charAt(i)) {
                        return Character.compare(arg1.charAt(i), arg0.charAt(i));
                    }
                    i++;
                }
                return 0;
            }
            
        });
        for (String n: nums) {
            pq.offer(n);
        }
        for (int i = 1; i < k; i++) {
            pq.poll();
        }
        return pq.poll();
    }
}

class Driver1985 {
    public static void main(String[] args) {
        String[] nums = {"3","6","7","10"};
        int k = 4;
        System.out.println((new Solution1985()).kthLargestNumber(nums, k));
    }
}
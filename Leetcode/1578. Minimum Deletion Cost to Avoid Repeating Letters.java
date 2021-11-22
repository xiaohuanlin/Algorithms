import java.util.*;

// Given a string s and an array of integers cost where cost[i] is the cost of deleting the ith character in s.

// Return the minimum cost of deletions such that there are no two identical letters next to each other.

// Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the costs of deleting other characters will not change.

 

// Example 1:

// Input: s = "abaac", cost = [1,2,3,4,5]
// Output: 3
// Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).
// Example 2:

// Input: s = "abc", cost = [1,2,3]
// Output: 0
// Explanation: You don't need to delete any character because there are no identical letters next to each other.
// Example 3:

// Input: s = "aabaa", cost = [1,2,3,4,1]
// Output: 2
// Explanation: Delete the first and the last character, getting the string ("aba").
 

// Constraints:

// s.length == cost.length
// 1 <= s.length, cost.length <= 10^5
// 1 <= cost[i] <= 10^4
// s contains only lowercase English letters.

class Solution1578 {
    public int minCost(String s, int[] cost) {
        int index = 0;
        int res = 0;
        while (index < s.length() - 1) {
            if (s.charAt(index) == s.charAt(index + 1)) {
                char c = s.charAt(index);
                int maxCost = cost[index];
                int sum = 0;
                while (index < s.length() && s.charAt(index) == c) {
                    maxCost = Math.max(maxCost, cost[index]);
                    sum += cost[index];
                    index++;
                }
                res += (sum - maxCost);
            } else {
                index++;
            }
        }
        return res;
    }
}

class Driver1578 {
    public static void main(String[] args) {
        Solution1578 solution = new Solution1578();

        String s = "abaac";
        int[] cost = {1,2,3,4,5};
        System.out.println(solution.minCost(s, cost));
    }
}
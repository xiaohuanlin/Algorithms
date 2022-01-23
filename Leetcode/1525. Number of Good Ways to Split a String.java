import java.util.*;

// You are given a string s.

// A split is called good if you can split s into two non-empty strings sleft and sright where their concatenation is equal to s (i.e., sleft + sright = s) and the number of distinct letters in sleft and sright is the same.

// Return the number of good splits you can make in s.

 

// Example 1:

// Input: s = "aacaba"
// Output: 2
// Explanation: There are 5 ways to split "aacaba" and 2 of them are good. 
// ("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
// ("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
// ("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
// ("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
// ("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.
// Example 2:

// Input: s = "abcd"
// Output: 1
// Explanation: Split the string as follows ("ab", "cd").
 

// Constraints:

// 1 <= s.length <= 105
// s consists of only lowercase English letters.

class Solution1525 {
    public int numSplits(String s) {
        Map<Character, Integer> left = new HashMap<>();
        Map<Character, Integer> right = new HashMap<>();

        for (char c: s.toCharArray()) {
            right.put(c, right.getOrDefault(c, 0) + 1);
        }

        int count = 0;
        for (char c: s.toCharArray()) {
            left.put(c, left.getOrDefault(c, 0) + 1);
            right.put(c, right.get(c) - 1);
            if (right.get(c) == 0) {
                right.remove(c);
            }

            if (left.size() == right.size()) {
                count++;
            }
        }
        return count;
    }
}

class Driver1525 {
    public static void main(String[] args) {
        String s = "aacaba";
        System.out.println(new Solution1525().numSplits(s));
    }
}
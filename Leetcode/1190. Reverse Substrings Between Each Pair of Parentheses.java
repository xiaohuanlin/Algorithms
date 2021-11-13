import java.util.*;

// You are given a string s that consists of lower case English letters and brackets. 

// Reverse the strings in each pair of matching parentheses, starting from the innermost one.

// Your result should not contain any brackets.

 

// Example 1:

// Input: s = "(abcd)"
// Output: "dcba"
// Example 2:

// Input: s = "(u(love)i)"
// Output: "iloveu"
// Explanation: The substring "love" is reversed first, then the whole string is reversed.
// Example 3:

// Input: s = "(ed(et(oc))el)"
// Output: "leetcode"
// Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
// Example 4:

// Input: s = "a(bcdefghijkl(mno)p)q"
// Output: "apmnolkjihgfedcbq"
 

// Constraints:

// 0 <= s.length <= 2000
// s only contains lower case English characters and parentheses.
// It's guaranteed that all parentheses are balanced.


class Solution1190 {
    public String reverseParentheses(String s) {
        Stack<Integer> candidates = new Stack<>();
        char[] res = s.toCharArray();

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                candidates.push(i);
            }
            if (s.charAt(i) == ')') {
                int start = candidates.pop();
                // reverse it
                int end = i;

                while (start < end) {
                    char tmp = res[start];
                    res[start++] = res[end];
                    res[end--] = tmp;
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for (char c: res) {
            if (c != '(' && c != ')') {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}

class Driver1190 {
    public static void main(String[] args) {
        Solution1190 solution = new Solution1190();

        String s = "(u(love)i)";
        System.out.println(solution.reverseParentheses(s));
    }
}
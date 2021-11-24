import java.util.*;

// Given a binary string s (a string consisting only of '0's and '1's), we can split s into 3 non-empty strings s1, s2, s3 (s1+ s2+ s3 = s).

// Return the number of ways s can be split such that the number of characters '1' is the same in s1, s2, and s3.

// Since the answer may be too large, return it modulo 10^9 + 7.

 

// Example 1:

// Input: s = "10101"
// Output: 4
// Explanation: There are four ways to split s in 3 parts where each part contain the same number of letters '1'.
// "1|010|1"
// "1|01|01"
// "10|10|1"
// "10|1|01"
// Example 2:

// Input: s = "1001"
// Output: 0
// Example 3:

// Input: s = "0000"
// Output: 3
// Explanation: There are three ways to split s in 3 parts.
// "0|0|00"
// "0|00|0"
// "00|0|0"
// Example 4:

// Input: s = "100100010100110"
// Output: 12
 

// Constraints:

// 3 <= s.length <= 10^5
// s[i] is '0' or '1'.

class Solution1573 {
    public int numWays(String s) {
        int count = 0;
        for (char c: s.toCharArray()) {
            if (c == '1') {
                count++;
            }
        }

        if (count % 3 != 0) {
            return 0;
        }

        if (count == 0) {
            return (int)(((long)(s.length() - 1) * (s.length() - 2) / 2) % (int)(1e9 + 7));
        }

        int numPerGroup = count / 3;
        count = 0;
        int start = 0;
        long left = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != '1') {
                continue;
            }
            count++;

            if (count == numPerGroup) {
                start = i;
            } else if (count == numPerGroup + 1) {
                left = i - start;
            }
            
            if (count == 2 * numPerGroup) {
                start = i;
            } else if (count == 2 * numPerGroup + 1) {
                left = left * (i - start);
            }
        }
        return (int)(left % (int)(1e9 + 7));
    }
}

class Driver1573 {
    public static void main(String[] args) {
        Solution1573 solution = new Solution1573();

        String s = "0000";
        System.out.println(solution.numWays(s));
    }
}
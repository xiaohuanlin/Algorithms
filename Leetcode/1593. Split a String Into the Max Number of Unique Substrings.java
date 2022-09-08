import java.util.*;

/*
Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
Example 2:

Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].
Example 3:

Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.
 

Constraints:

1 <= s.length <= 16

s contains only lower case English letters.
*/

class Solution1593 {
    private String s;
    private int res;
    
    private void backtrace(int start, Set<String> visit) {
        for (int i = start+1; i <= s.length(); i++) {
            String tmp = s.substring(start, i);
            if (!visit.contains(tmp)) {
                visit.add(tmp);
                backtrace(i, visit);
                visit.remove(tmp);
            }
        }
        res = Math.max(res, visit.size());
    }
    
    public int maxUniqueSplit(String s) {
        this.s = s;
        Set<String> visit = new HashSet<>();
        backtrace(0, visit);
        return res;
    }
}

class Driver1593 {
    public static void main(String[] args) {
        String t = "ababccc";
        System.out.println(new Solution1593().maxUniqueSplit(t));
    }
}
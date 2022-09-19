import java.util.*;

/*
Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.

You may return the answer in any order.

 

Example 1:

Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 

Constraints:

2 <= n <= 9
0 <= k <= 9
 */

class Solution967 {
    private List<Integer> res = new ArrayList<>();
    
    public void backtrace(int i, int k, int limit, List<Integer> path) {
        if (limit == 0) {
            int r = 0;
            for (int n: path) {
                r = r * 10 + n;
            }
            res.add(r);
            return;
        }

        if (i + k < 10 && i + k >= 0) {
            path.add(i+k);
            backtrace(i+k, k, limit - 1, path);
            path.remove(path.size() - 1);
        }
        if (k != 0 && i - k < 10 && i - k >= 0) {
            path.add(i-k);
            backtrace(i-k, k, limit - 1, path);
            path.remove(path.size() - 1);
        }
    }
    
    public int[] numsSameConsecDiff(int n, int k) {
        for (int i = 1; i < 10; i++) {
            backtrace(i, k, n-1, new ArrayList<>(Arrays.asList(i)));
        }
        return res.stream().mapToInt(i->i).toArray();
    }
}

class Driver967 {
    public static void main(String[] args) {
        System.out.println(new Solution967().numsSameConsecDiff(3, 7));
    }
}
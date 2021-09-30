import java.util.Arrays;
import java.util.Comparator;


// You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

// One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

// Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

// Note: You cannot rotate an envelope.

 

// Example 1:

// Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
// Output: 3
// Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
// Example 2:

// Input: envelopes = [[1,1],[1,1],[1,1]]
// Output: 1
 

// Constraints:

// 1 <= envelopes.length <= 5000
// envelopes[i].length == 2
// 1 <= wi, hi <= 10^4

class Solution354 {
    public int maxEnvelopes(int[][] envelopes) {
        Arrays.sort(envelopes, new Comparator<int[]>() {
            @Override
            public int compare(int[] a, int[] b) {
                if (a[0] == b[0]) {
                    return a[1] - b[1];
                } else {
                    return a[0] - b[0];
                }
            };
        });

        int[] dp = new int[envelopes.length];
        dp[0] = 1;
        for (int i = 1; i < dp.length; i++) {
            int maxV = 1;
            for (int j = 0; j < i; j++) {
                if (envelopes[i][0] > envelopes[j][0] && envelopes[i][1] > envelopes[j][1]) {
                    if (dp[j] + 1 > maxV) {
                        maxV = dp[j] + 1;
                    }
                }
            }
            dp[i] = maxV;
        }

        int res = Integer.MIN_VALUE;
        for (int i = 0; i < dp.length; i++) {
            if (dp[i] > res) {
                res = dp[i];
            }
        }
        return res;
    }
}

class Driver354 {
    public static void main(String[] args) {
        Solution354 solution = new Solution354();

        int [][] testCase = {{10,8},{1,12},{6,15},{2,18}};
        System.out.println(solution.maxEnvelopes(testCase));
    }
}
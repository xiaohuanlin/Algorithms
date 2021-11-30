import java.util.*;


// There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

// You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

 

// Example 1:


// Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
// Output: 200
// Explanation: The graph is shown.
// The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
// Example 2:


// Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
// Output: 500
// Explanation: The graph is shown.
// The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
 

// Constraints:

// 1 <= n <= 100
// 0 <= flights.length <= (n * (n - 1) / 2)
// flights[i].length == 3
// 0 <= fromi, toi < n
// fromi != toi
// 1 <= pricei <= 104
// There will not be any multiple flights between two cities.
// 0 <= src, dst, k < n
// src != dst


class Solution787 {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        int[][] dp = new int[k+2][n];
        for (int i = 0; i < k + 2; i++) {
            for (int j = 0; j < n; j++) {
                dp[i][j] = Integer.MAX_VALUE;
            }
        }

        for (int i = 0; i < k + 2; i++) {
            dp[i][src] = 0;
        }

        for (int i = 1; i < k + 2; i++) {
            for (int[] flight: flights) {
                int start = flight[0];
                int end = flight[1];
                int price = flight[2];
                if (dp[i - 1][start] != Integer.MAX_VALUE) {
                    dp[i][end] = Math.min(dp[i][end], dp[i - 1][start] + price);
                }
            }
        }
        return dp[k+1][dst] == Integer.MAX_VALUE ? -1 : dp[k+1][dst];
    }
}

class Driver787 {
    public static void main(String[] args) {
        int n = 4;
        int[][] flights = {{0, 1, 1}, {0, 2, 5}, {1, 2, 1}, {2, 3, 1}};
        int src = 0;
        int dst = 3;
        int k = 1;
        System.out.println((new Solution787()).findCheapestPrice(n, flights, src, dst, k));
    }
}
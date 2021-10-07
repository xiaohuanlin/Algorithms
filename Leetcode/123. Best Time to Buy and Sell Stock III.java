// You are given an array prices where prices[i] is the price of a given stock on the ith day.

// Find the maximum profit you can achieve. You may complete at most two transactions.

// Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

// Example 1:

// Input: prices = [3,3,5,0,0,3,1,4]
// Output: 6
// Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
// Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
// Example 2:

// Input: prices = [1,2,3,4,5]
// Output: 4
// Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
// Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
// Example 3:

// Input: prices = [7,6,4,3,1]
// Output: 0
// Explanation: In this case, no transaction is done, i.e. max profit = 0.
// Example 4:

// Input: prices = [1]
// Output: 0
 

// Constraints:

// 1 <= prices.length <= 10^5
// 0 <= prices[i] <= 10^5


class Solution123 {
    public int maxProfit(int[] prices) {
        int maxPro = 0;

        int rightMaxPro = 0;
        int rightMax = prices[prices.length - 1];
        int[] rightMaxArray = new int[prices.length];
        for (int i = prices.length - 1; i >= 0; i--) {
            rightMaxPro = Math.max(rightMax - prices[i], rightMaxPro);
            rightMax = Math.max(prices[i], rightMax);
            rightMaxArray[i] = rightMaxPro;
        }

        int leftMin = prices[0];
        for (int i = 0; i < prices.length; i++) {
            // choose i as the end date of first transaction
            int leftProfit = Math.max(prices[i] - leftMin, 0);
            leftMin = Math.min(leftMin, prices[i]);
            
            maxPro = Math.max(leftProfit + rightMaxArray[i], maxPro);
        }
        return maxPro;
    }
}

class Driver123 {
    public static void main(String[] args) {
        Solution123 solution = new Solution123();

        int[] prices = {1,2,3,4,5};
        System.out.println(solution.maxProfit(prices));
    }
}
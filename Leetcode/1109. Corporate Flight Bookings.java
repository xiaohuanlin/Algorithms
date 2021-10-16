import java.util.*;

// There are n flights that are labeled from 1 to n.

// You are given an array of flight bookings bookings, where bookings[i] = [firsti, lasti, seatsi] represents a booking for flights firsti through lasti (inclusive) with seatsi seats reserved for each flight in the range.

// Return an array answer of length n, where answer[i] is the total number of seats reserved for flight i.

 

// Example 1:

// Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
// Output: [10,55,45,25,25]
// Explanation:
// Flight labels:        1   2   3   4   5
// Booking 1 reserved:  10  10
// Booking 2 reserved:      20  20
// Booking 3 reserved:      25  25  25  25
// Total seats:         10  55  45  25  25
// Hence, answer = [10,55,45,25,25]
// Example 2:

// Input: bookings = [[1,2,10],[2,2,15]], n = 2
// Output: [10,25]
// Explanation:
// Flight labels:        1   2
// Booking 1 reserved:  10  10
// Booking 2 reserved:      15
// Total seats:         10  25
// Hence, answer = [10,25]

 

// Constraints:

// 1 <= n <= 2 * 10^4
// 1 <= bookings.length <= 2 * 10^4
// bookings[i].length == 3
// 1 <= firsti <= lasti <= n
// 1 <= seatsi <= 10^4

class Solution1109 {
    public int[] corpFlightBookings(int[][] bookings, int n) {
        int[] res = new int[n];
        for (int[] booking: bookings) {
            int start = booking[0] - 1;
            int end = booking[1];

            res[start] += booking[2];
            if (end < n) {
                res[end] -= booking[2];
            }
        }

        for (int i = 1; i < n; i++) {
            res[i] = res[i] + res[i - 1];
        }
        return res;
    }
}

class Driver1109 {
    public static void main(String[] args) {
        Solution1109 solution = new Solution1109();

        int[][] bookings = {{1,2,10}, {2,3,20}, {2,5,25}};
        int n = 5;
        System.out.println(Arrays.toString(solution.corpFlightBookings(bookings, n)));
    }
}
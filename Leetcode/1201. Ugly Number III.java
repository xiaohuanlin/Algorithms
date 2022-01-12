import java.util.*;

// An ugly number is a positive integer that is divisible by a, b, or c.

// Given four integers n, a, b, and c, return the nth ugly number.

 

// Example 1:

// Input: n = 3, a = 2, b = 3, c = 5
// Output: 4
// Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
// Example 2:

// Input: n = 4, a = 2, b = 3, c = 4
// Output: 6
// Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.
// Example 3:

// Input: n = 5, a = 2, b = 11, c = 13
// Output: 10
// Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
 

// Constraints:

// 1 <= n, a, b, c <= 109
// 1 <= a * b * c <= 1018
// It is guaranteed that the result will be in range [1, 2 * 109].

class Solution1201 {
    public long getGcd(long a, long b) {
        if (a == 0) {
            return b;
        }
        return getGcd(b % a, a);
    }

    public long getLcm(long a, long b) {
        return a * b / getGcd(a, b);
    }

    public long getLcm(long a, long b, long c) {
        return getLcm(a, getLcm(b, c));
    }

    public int getUglyNumber(long k, long a, long b, long c) {
        return (int)(k / a + k / b + k / c - k / getLcm(a, b) - k / getLcm(b, c) - k / getLcm(a, c) + k / getLcm(a, b, c));
    }

    public int nthUglyNumber(int n, int a, int b, int c) {
        int start = 1;
        int end = 2 * 1_000_000_000;

        while (start < end) {
            int middle = (end - start) / 2 + start;
            if (getUglyNumber(middle, a, b, c) < n) {
                start = middle + 1;
            } else {
                end = middle;
            }
        }
        return start;
    }
}

class Driver1201 {
    public static void main(String[] args) {
        System.out.println(new Solution1201().nthUglyNumber(1000000000, 2, 217983653, 336916467));
    }
}
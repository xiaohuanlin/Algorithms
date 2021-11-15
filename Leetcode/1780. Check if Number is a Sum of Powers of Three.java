
// Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

// An integer y is a power of three if there exists an integer x such that y == 3x.

 

// Example 1:

// Input: n = 12
// Output: true
// Explanation: 12 = 31 + 32
// Example 2:

// Input: n = 91
// Output: true
// Explanation: 91 = 30 + 32 + 34
// Example 3:

// Input: n = 21
// Output: false
 

// Constraints:

// 1 <= n <= 107

class Solution1780 {
    public boolean checkPowersOfThree(int n) {
        while (n != 0) {
            if (n % 3 == 2) {
                return false;
            }
            n /= 3;
        }
        return true;
    }
}

class Driver1780 {
    public static void main(String[] args) {
        Solution1780 solution = new Solution1780();

        int n = 1;
        System.out.println(solution.checkPowersOfThree(n));
    }
}
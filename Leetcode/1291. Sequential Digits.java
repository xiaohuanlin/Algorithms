import java.util.*;

// An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

// Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

// Example 1:

// Input: low = 100, high = 300
// Output: [123,234]
// Example 2:

// Input: low = 1000, high = 13000
// Output: [1234,2345,3456,4567,5678,6789,12345]
 

// Constraints:

// 10 <= low <= high <= 10^9


class Solution1291 {
    public List<Integer> sequentialDigits(int low, int high) {
        int startSize = String.valueOf(low).length();

        List<Integer> res = new ArrayList<>();
        int startValue = 0;
        int delta = 0;
        int limit = 0;
        for (int i = 1; i <= startSize; i++) {
            startValue = 10 * startValue + i;
            delta = 10 * delta + 1;
            limit = 10 * limit + 9;
        }

        for (int i = startSize + 1;; i++) {
            int iterValue = startValue;
            while (iterValue < limit && iterValue % 10 != 0) {
                if (iterValue > high) {
                    return res;
                }
                if (iterValue >= low) {
                    res.add(iterValue);
                }
                iterValue += delta;
            }

            startValue = 10 * startValue + i;
            limit = 10 * limit + 9;
            delta = 10 * delta + 1;
        }
    }
}

class Driver1291 {
    public static void main(String[] args) {
        int low = 1000;
        int high = 13000;
        System.out.println((new Solution1291()).sequentialDigits(low, high));
    }
}
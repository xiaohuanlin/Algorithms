import java.util.*;
import java.util.concurrent.CountDownLatch;

// A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.

// You can pick any two different foods to make a good meal.

// Given an array of integers deliciousness where deliciousness[i] is the deliciousness of the i​​​​​​th​​​​​​​​ item of food, return the number of different good meals you can make from this list modulo 109 + 7.

// Note that items with different indices are considered different even if they have the same deliciousness value.

 

// Example 1:

// Input: deliciousness = [1,3,5,7,9]
// Output: 4
// Explanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).
// Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.
// Example 2:

// Input: deliciousness = [1,1,1,3,3,3,7]
// Output: 15
// Explanation: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and (1,7) with 3 ways.
 

// Constraints:

// 1 <= deliciousness.length <= 10^5
// 0 <= deliciousness[i] <= 2^20

class Solution1711 {
    public int countPairs(int[] deliciousness) {
        int[] allTwoPower = new int[22];
        allTwoPower[0] = 1;
        for (int i = 1; i < 22; i++) {
            allTwoPower[i] = allTwoPower[i - 1] * 2;
        }

        Map<Integer, Integer> counts = new TreeMap<>();
        for (int de: deliciousness) {
            counts.put(de, counts.getOrDefault(de, 0) + 1);
        }

        long res = 0;
        for (int de: counts.keySet()) {
            for (int power: allTwoPower) {
                int target = power - de;
                if (target >= de && counts.containsKey(target)) {
                    if (target == de) {
                        res += ((long)counts.get(de) * (counts.get(de) - 1) / 2);
                    } else {
                        res += (long)counts.get(de) * counts.get(target);
                    }
                    res %= (1_000_000_000 + 7);
                }
            }
        }
        return (int)res;
    }
}

class Driver1711 {
    public static void main(String[] args) {
        int[] deliciousness = new int[10000];
        for (int i = 0; i < 10000; i++) {
            deliciousness[i] = 32;
        }
        System.out.println((new Solution1711()).countPairs(deliciousness));
    }
}
import java.util.*;

// There is an integer array perm that is a permutation of the first n positive integers, where n is always odd.

// It was encoded into another integer array encoded of length n - 1, such that encoded[i] = perm[i] XOR perm[i + 1]. For example, if perm = [1,3,2], then encoded = [2,1].

// Given the encoded array, return the original array perm. It is guaranteed that the answer exists and is unique.

 

// Example 1:

// Input: encoded = [3,1]
// Output: [1,2,3]
// Explanation: If perm = [1,2,3], then encoded = [1 XOR 2,2 XOR 3] = [3,1]
// Example 2:

// Input: encoded = [6,5,4,6]
// Output: [2,4,1,5,3]
 

// Constraints:

// 3 <= n < 10^5
// n is odd.
// encoded.length == n - 1

class Solution1734 {
    public int[] decode(int[] encoded) {
        // we calculate b xor c xor d ...
        int xorProductExceptForA = 0;
        int xorProductAXorCurrent = 0;
        int xorProductTotal = 1;

        for (int i = 0; i < encoded.length; i++) {
            xorProductTotal ^= (i + 2);
            xorProductAXorCurrent ^= encoded[i];
            xorProductExceptForA ^= xorProductAXorCurrent;
        }

        int[] res = new int[encoded.length + 1];
        // get result of a
        res[0] = xorProductTotal ^ xorProductExceptForA;
        for (int i = 0; i < encoded.length; i++) {
            res[i + 1] = res[i] ^ encoded[i];
        }
        return res;
    }
}

class Driver1734 {
    public static void main(String[] args) {
        int[] encoded = {3,1};
        System.out.println((new Solution1734()).decode(encoded));
    }
}
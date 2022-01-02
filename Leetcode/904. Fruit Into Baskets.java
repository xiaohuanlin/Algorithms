import java.util.*;

import javax.swing.text.AbstractDocument.LeafElement;

// You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

// You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

// You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
// Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
// Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
// Given the integer array fruits, return the maximum number of fruits you can pick.

 

// Example 1:

// Input: fruits = [1,2,1]
// Output: 3
// Explanation: We can pick from all 3 trees.
// Example 2:

// Input: fruits = [0,1,2,2]
// Output: 3
// Explanation: We can pick from trees [1,2,2].
// If we had started at the first tree, we would only pick from trees [0,1].
// Example 3:

// Input: fruits = [1,2,3,2,2]
// Output: 4
// Explanation: We can pick from trees [2,3,2,2].
// If we had started at the first tree, we would only pick from trees [1,2].
 

// Constraints:

// 1 <= fruits.length <= 10^5
// 0 <= fruits[i] < fruits.length

class Solution904 {
    public int totalFruit(int[] fruits) {
        int start = 0;
        int end = 0;

        int res = 0;
        int sum = 0;
        int kind = 0;
        int[] windows = new int[fruits.length];

        while (start < fruits.length && end < fruits.length) {
            if (kind <= 2) {
                // expend
                windows[fruits[end]]++;
                if (windows[fruits[end]] == 1) {
                    kind++;
                }
                sum++;
                end++;

                if (kind <= 2) {
                    res = Math.max(res, sum);
                }
            } else {
                // shrink
                windows[fruits[start]]--;
                if (windows[fruits[start]] == 0) {
                    kind--;
                }
                sum--;
                start++;
            }
        }
        return res;
    }
}

class Driver904 {
    public static void main(String[] args) {
        int[] fruits = {3,3,3,1,2,1,1,2,3,3,4};
        System.out.println((new Solution904()).totalFruit(fruits));
    }
}
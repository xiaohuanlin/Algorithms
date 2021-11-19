import java.io.FileReader;
import java.util.*;

// Given two numbers arr1 and arr2 in base -2, return the result of adding them together.

// Each number is given in array format:  as an array of 0s and 1s, from most significant bit to least significant bit.  For example, arr = [1,1,0,1] represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.  A number arr in array, format is also guaranteed to have no leading zeros: either arr == [0] or arr[0] == 1.

// Return the result of adding arr1 and arr2 in the same format: as an array of 0s and 1s with no leading zeros.

 

// Example 1:

// Input: arr1 = [1,1,1,1,1], arr2 = [1,0,1]
// Output: [1,0,0,0,0]
// Explanation: arr1 represents 11, arr2 represents 5, the output represents 16.
// Example 2:

// Input: arr1 = [0], arr2 = [0]
// Output: [0]
// Example 3:

// Input: arr1 = [0], arr2 = [1]
// Output: [1]
 

// Constraints:

// 1 <= arr1.length, arr2.length <= 1000
// arr1[i] and arr2[i] are 0 or 1
// arr1 and arr2 have no leading zeros

class Solution1073 {
    public int[] addNegabinary(int[] arr1, int[] arr2) {
        int i = arr1.length - 1;
        int j = arr2.length - 1;
        int[] res = new int[Math.max(i, j) + 3];
        int k = res.length - 1;
        while (k >= 0) {
            int left = i >= 0 ? arr1[i]: 0;
            int right = j >= 0 ? arr2[j]: 0;
            res[k] = left + right + res[k];
            if (res[k] == -1) {
                res[k] = 1;
                res[k - 1] = 1;
            } else if (res[k] == 0 || res[k] == 1) {
            } else if (res[k] == 2) {
                res[k] = 0;
                res[k - 1] = -1;
            } else if (res[k] == 3) {
                res[k] = 1;
                res[k - 1] = -1;
            }
            i--;
            j--;
            k--;
        }

        int first_one = -1;
        int count = 0;
        for (int m = 0; m < res.length; m++) {
            if (res[m] == 1 && first_one == -1) {
                first_one = m;
            }
            count++;
        }
        if (first_one == -1) {
            int[] ans = {0};
            return ans;
        }

        int[] ans = new int[count - first_one];
        for (int m = first_one; m < res.length; m++) {
            ans[m - first_one] = res[m];
        }
        System.out.println(Arrays.toString(ans));
        return ans;
    }
}

class Driver1073 {
    public static void main(String[] args) {
        Solution1073 solution = new Solution1073();

        int[] arr1 = {1,1,1,1,1};
        int[] arr2 = {1,0,1};
        System.out.println(solution.addNegabinary(arr1, arr2));
    }
}
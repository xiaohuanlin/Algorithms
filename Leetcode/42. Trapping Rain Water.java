
// Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

// Example 1:


// Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
// Output: 6
// Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
// Example 2:

// Input: height = [4,2,0,3,2,5]
// Output: 9
 

// Constraints:

// n == height.length
// 1 <= n <= 2 * 10^4
// 0 <= height[i] <= 10^5


class Solution42 {
    public int trap(int[] height) {
        int[] rightMaxArray = new int[height.length + 1];
        for (int i = height.length - 1; i >= 0; i--) {
            rightMaxArray[i] = Math.max(rightMaxArray[i+1], height[i]);
        }

        int leftMax = 0;
        int sum = 0;
        for (int i = 1; i < height.length - 1; i++) {
            leftMax = Math.max(leftMax, height[i-1]);
            int minMax = Math.min(leftMax, rightMaxArray[i+1]);
            if (minMax > height[i]) {
                sum += (minMax - height[i]);
            }
        }
        return sum;
    }
}

class Driver42 {
    public static void main(String[] args) {
        Solution42 solution = new Solution42();

        int[] height = {0,2,0};
        System.out.println(solution.trap(height));
    }
}
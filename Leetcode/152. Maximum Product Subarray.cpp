#include <unordered_set>
#include <unordered_map>
#include <math.h>
#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;


// Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

// Example 1:

// Input: [2,3,-2,4]
// Output: 6
// Explanation: [2,3] has the largest product 6.
// Example 2:

// Input: [-2,0,-1]
// Output: 0
// Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

 
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int size = nums.size();
        if (size == 0) {
            return 0;
        }
        vector<vector<int>> dp(size, vector<int>(size, 0));
        vector<vector<int>> multi(size, vector<int>(size, 0));

        for (int end = 0; end < size; end++) {
            for (int start = end; start >= 0; start--) {
                if (start == end) {
                    dp[start][end] = nums[start];
                    multi[start][end] = nums[start];
                } else {
                    multi[start][end] = multi[start+1][end] * nums[start];
                    // deal with for multiply the element
                    int max = nums[end];
                    for (int k = end-1; k >= start; k--) {
                        if (max < multi[k][end]) {
                            max = multi[k][end];
                        }
                    }

                    // deal with others
                    if (max < dp[start+1][end]) {
                        max = dp[start+1][end];
                    }

                    if (max < dp[start][end-1]) {
                        max = dp[start][end-1];
                    }
                    dp[start][end] = max;
                }
            }
        }
        return dp[0][size-1];
    }

    int maxProductNew(vector<int>& nums) {
        int left_count = 0;
        int left_sum = 1;
        int size = nums.size();
        int right_count = size - 1;
        int right_sum = 1;
        while (left_count < size && nums[left_count] > 0) {
            left_sum *= nums[left_count++];
        }

        if (left_count == size) {
            return left_sum;
        }

        while (right_count >= 0 && nums[right_count] > 0) {
            right_sum *= nums[right_count--];
        }

        if (left_count == right_count) {
            return left_sum > right_sum ? left_sum: right_sum;
        }

        int middle_sum = 1;
        int middle = left_count + 1;
        while (middle < right_count) {
            middle_sum *= nums[middle];
        }

        if (middle_sum > 0) {
            return left_sum * nums[left_count] * middle_sum * nums[right_count] * right_sum;
        } else if (middle_sum == 0) {
            return left_sum > right_sum ? left_sum: right_sum;
        } else {
            left_sum = left_sum * nums[left_count] * middle_sum;
            right_sum = right_sum* nums[right_count] * middle_sum;
            return left_sum > right_sum ? left_sum: right_sum;
        }

    }


    int maxProductNew2(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        }

        int positive_max = nums[0];
        int negetive_min = nums[0];
        int max_value = nums[0];
        
        for (int i = 1; i < nums.size(); i++) {

            if (nums[i] > 0) {
                positive_max = max(positive_max * nums[i], nums[i]);
                negetive_min = min(negetive_min * nums[i], nums[i]);
            } else {
                int tmp = positive_max;
                positive_max = max(negetive_min * nums[i], nums[i]);
                negetive_min = min(tmp * nums[i], nums[i]);
            }
            max_value = max(max_value, positive_max);
        }

        return max_value;
    }
};

int main() {
    Solution s;
    vector<int> array = {-1, -2, -3, 4, -5};
    cout << s.maxProductNew2(array);
}
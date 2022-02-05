#include <vector>
#include <stack>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// Given an integer array arr and an integer k, modify the array by repeating it k times.

// For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

// Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.

// As the answer can be very large, return the answer modulo 109 + 7.

 

// Example 1:

// Input: arr = [1,2], k = 3
// Output: 9
// Example 2:

// Input: arr = [1,-2,1], k = 5
// Output: 2
// Example 3:

// Input: arr = [-1,-2], k = 7
// Output: 0
 

// Constraints:

// 1 <= arr.length <= 105
// 1 <= k <= 105
// -104 <= arr[i] <= 104


class Solution {
public:
    int kConcatenationMaxSum(vector<int>& arr, int k) {
        int leftMax = 0;
        long leftMaxSum = 0;
        long leftSumValue = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (leftMaxSum < leftSumValue + arr[i]) {
                leftMax = i;
                leftMaxSum = leftSumValue + arr[i];
            }
            leftSumValue += arr[i];
        }

        int rightMax = 0;
        long rightMaxSum = 0;
        long rightSumValue = 0;
        for (int i = arr.size() - 1; i >= 0; i--) {
            if (rightMaxSum < rightSumValue + arr[i]) {
                rightMax = i;
                rightMaxSum = rightSumValue + arr[i];
            }
            rightSumValue += arr[i];
        }

        long subarrayMaxSum = calculateMaxSum(arr);

        if (k == 1) {
            return max(max(leftMaxSum, rightMaxSum), subarrayMaxSum);
        } else {
            if (leftSumValue > 0) {
                return max(
                    max(
                        (k - 2) * leftSumValue + leftMaxSum + rightMaxSum, 
                        max(((k - 1) * leftSumValue + leftMaxSum), ((k - 1) * leftSumValue + rightMaxSum))
                    ),
                    subarrayMaxSum) % int(1e9 + 7);
            }
            return max((leftMaxSum + rightMaxSum), subarrayMaxSum) % int(1e9 + 7);
        }
    }

    long calculateMaxSum(vector<int>& array) {
        long res = 0;
        long currentSum = 0;
        for (long num: array) {
            currentSum = max(currentSum + num, num);
            res = max(res, currentSum);
        }
        return res;
    }
};

int main() {
    Solution s;
    vector<
        tuple<
            tuple<vector<int>, int>, 
            int
        >
    > test_cases {
        {
            {{1,2}, 3},
            9
        },
        {
            {{1,-2,1}, 5},
            2
        },
        {
            {{-1,-2}, 7},
            0
        },
        {
            {{2,-5,2}, 7},
            4
        },
    };

    for (auto& test_case: test_cases) {
        assert(s.kConcatenationMaxSum(
                    get<0>(get<0>(test_case)),
                    get<1>(get<0>(test_case))
                ) == get<1>(test_case)
        );
    }
}
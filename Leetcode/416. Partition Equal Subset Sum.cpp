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
#include <queue>
using namespace std;


// Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

// Note:

// Each of the array element will not exceed 100.
// The array size will not exceed 200.
 

// Example 1:

// Input: [1, 5, 11, 5]

// Output: true

// Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

// Example 2:

// Input: [1, 2, 3, 5]

// Output: false

// Explanation: The array cannot be partitioned into equal sum subsets.


class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = 0;
        for (auto &ele: nums) {
            sum += ele;
        }
        if (sum % 2 != 0) {
            return false;
        }
        return backtrace(0, sum/2, nums);
    }

    bool backtrace(int sum, int target, vector<int> &candidate) {
        if (sum == target) {
            return true;
        } else if (sum > target) {
            return false;
        }

        int size = candidate.size();
        for (int i = 0; i < size; i++) {
            int value = candidate[i];
            candidate.erase(candidate.cbegin() + i);
            if (backtrace(sum + value, target, candidate)) {
                return true;
            }
            candidate.insert(candidate.cbegin() + i, value);
        }
        return false;
    }
};

int main() {
    Solution s;
    vector<int> array = {1,5,11,5};
    cout << s.canPartition(array);
    // todo
}

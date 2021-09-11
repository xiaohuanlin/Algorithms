#include <vector>
#include <set>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// We have an array arr of non-negative integers.

// For every (contiguous) subarray sub = [arr[i], arr[i + 1], ..., arr[j]] (with i <= j), we take the bitwise OR of all the elements in sub, obtaining a result arr[i] | arr[i + 1] | ... | arr[j].

// Return the number of possible results. Results that occur more than once are only counted once in the final answer

 

// Example 1:

// Input: arr = [0]
// Output: 1
// Explanation: There is only one possible result: 0.
// Example 2:

// Input: arr = [1,1,2]
// Output: 3
// Explanation: The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
// These yield the results 1, 1, 2, 1, 3, 3.
// There are 3 unique values, so the answer is 3.
// Example 3:

// Input: arr = [1,2,4]
// Output: 6
// Explanation: The possible results are 1, 2, 3, 4, 6, and 7.
 

// Constraints:

// 1 <= nums.length <= 5 * 10^4
// 0 <= nums[i] <= 10^9

// Given a balance

class Solution {
public:
    int subarrayBitwiseORs(vector<int>& arr) {
        set<int> res, store;
        for (auto& num: arr) {
            set<int> tmp {num};
            for (auto& v: store) {
                tmp.insert(v | num);
            }
            store = tmp;
            // store the result
            for (auto& v: store) {
                res.insert(v);
            }
        }
        return res.size();
    }
};


int main() {
    Solution s;
    vector<tuple<vector<int>, int>> test_cases {
        {{0}, 1},
        {{1,1,2}, 3},
        {{1,2,4}, 6},
    };

    for (auto& test_case: test_cases) {
        assert(s.subarrayBitwiseORs(get<0>(test_case)) == get<1>(test_case));
    }
}
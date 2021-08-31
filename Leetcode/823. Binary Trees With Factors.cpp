#include <vector>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;


// Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

// We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

// Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

 

// Example 1:

// Input: arr = [2,4]
// Output: 3
// Explanation: We can make these trees: [2], [4], [4, 2, 2]
// Example 2:

// Input: arr = [2,4,5,10]
// Output: 7
// Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
 

// Constraints:

// 1 <= arr.length <= 1000
// 2 <= arr[i] <= 10^9
// All the values of arr are unique.


class Solution {
public:
    int numFactoredBinaryTrees(vector<int>& arr) {
        unordered_map<int, long> maps;
        sort(arr.begin(), arr.end());
        int modulo = int(1e9) + 7;
        int result = 0;
        for (int i = 0; i < arr.size(); i++) {
            maps[arr[i]] = 1;
            for (int j = 0; j < i; j++) {
                if (arr[i] % arr[j] == 0 && maps.find(arr[i] / arr[j]) != maps.end()) {
                    maps[arr[i]] += ((maps[arr[j]] % modulo) * (maps[arr[i] / arr[j]] % modulo)) % modulo;
                    maps[arr[i]] %= modulo;
                }
            }
            result += maps[arr[i]];
            result %= modulo;
        }
        return result;
    }
};


int main() {
    Solution s;
    vector<tuple<vector<int>, int>> test_cases {
        {{18, 3, 6, 2}, 12},
        {{2, 4}, 3},
        {{2, 4, 5, 10}, 7},
    };

    for (auto& test_case: test_cases) {
        assert(s.numFactoredBinaryTrees(get<0>(test_case)) == get<1>(test_case));
    }
}
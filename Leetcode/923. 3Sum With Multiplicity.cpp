#include <vector>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;


// Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

// As the answer can be very large, return it modulo 109 + 7.

 

// Example 1:

// Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
// Output: 20
// Explanation: 
// Enumerating by the values (arr[i], arr[j], arr[k]):
// (1, 2, 5) occurs 8 times;
// (1, 3, 4) occurs 8 times;
// (2, 2, 4) occurs 2 times;
// (2, 3, 3) occurs 2 times.
// Example 2:

// Input: arr = [1,1,2,2,2,2], target = 5
// Output: 12
// Explanation: 
// arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
// We choose one 1 from [1,1] in 2 ways,
// and two 2s from [2,2,2,2] in 6 ways.
 

// Constraints:

// 3 <= arr.length <= 3000
// 0 <= arr[i] <= 100
// 0 <= target <= 300


class Solution {
public:
    int threeSumMulti(vector<int>& arr, int target) {
        unordered_map<int, long> counts;
        for (auto& number: arr) {
            counts[number]++;
        }

        long result = 0;
        for (auto& iter1: counts) {
            for (auto& iter2: counts) {
                int i = iter1.first;
                int j = iter2.first;
                int k = target - i - j;

                if (counts.find(k) == counts.end()) {
                    continue;
                }

                if (i < j && j < k) {
                    // all numbers are unique 
                    result += counts[i] * counts[j] * counts[k];
                } else if (i == j && j != k) {
                    // two numbers are the same
                    result += counts[i] * (counts[i] - 1) / 2 * counts[k];
                } else if (i == j && j == k){
                    // all same
                    result += counts[i] * (counts[i] - 1) * (counts[i] - 2) / 6;
                }
            }
        }
        
        return result % int(1e9 + 7);
    }
};


int main() {
    Solution s;
    vector<tuple<tuple<vector<int>, int>, int>> test_cases {
        {{{1,1,2,2,3,3,4,4,5,5}, 8}, 20},
        {{{1,1,2,2,2,2}, 5}, 12},
    };

    for (auto& test_case: test_cases) {
        assert(s.threeSumMulti(get<0>(get<0>(test_case)),get<1>(get<0>(test_case))) == get<1>(test_case));
    }
}
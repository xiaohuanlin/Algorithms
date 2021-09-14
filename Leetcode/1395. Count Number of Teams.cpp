#include <vector>
#include <stack>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

// You have to form a team of 3 soldiers amongst them under the following rules:

// Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
// A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
// Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

// Example 1:

// Input: rating = [2,5,3,4,1]
// Output: 3
// Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
// Example 2:

// Input: rating = [2,1,3]
// Output: 0
// Explanation: We can't form any team given the conditions.
// Example 3:

// Input: rating = [1,2,3,4]
// Output: 4
 

// Constraints:

// n == rating.length
// 3 <= n <= 1000
// 1 <= rating[i] <= 10^5
// All the integers in rating are unique.


class Solution {
public:
    int numTeams(vector<int>& rating) {
        unordered_map<int, vector<int>> max_maps;
        unordered_map<int, vector<int>> min_maps;

        for (int i = 0; i < rating.size(); i++) {
            for (int j = i+1; j < rating.size(); j++) {
                if (rating[j] > rating[i]) {
                    max_maps[i].push_back(j);
                } else {
                    min_maps[i].push_back(j);
                }
            }
        }

        int count = 0;
        // formate the team
        for (int i = 0; i < rating.size(); i++) {
            for (auto& j: max_maps[i]) {
                count += max_maps[j].size();
            }

            for (auto& j: min_maps[i]) {
                count += min_maps[j].size();
            }
        }
        return count;
    }
};

int main() {
    Solution s;
    vector<tuple<vector<int>, int>> test_cases {
        {{2,5,3,4,1}, 3},
        {{2,1,3}, 0},
        {{1,2,3,4}, 4}
    };

    for (auto& test_case: test_cases) {
        assert(s.numTeams(get<0>(test_case)) == get<1>(test_case));
    }
}
#include <vector>
#include <set>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;


// Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or equal to bound.

// An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.

// You may return the answer in any order. In your answer, each value should occur at most once.

 

// Example 1:

// Input: x = 2, y = 3, bound = 10
// Output: [2,3,4,5,7,9,10]
// Explanation:
// 2 = 20 + 30
// 3 = 21 + 30
// 4 = 20 + 31
// 5 = 21 + 31
// 7 = 22 + 31
// 9 = 23 + 30
// 10 = 20 + 32
// Example 2:

// Input: x = 3, y = 5, bound = 15
// Output: [2,4,6,8,10,14]
 

// Constraints:

// 1 <= x, y <= 100
// 0 <= bound <= 10^6

class Solution {
public:
    vector<int> powerfulIntegers(int x, int y, int bound) {
        vector<int> x_power;
        vector<int> y_power;
        int x_current = 1;
        int y_current = 1;

        while (x_current < bound) {
            x_power.push_back(x_current);
            x_current *= x;
            if (x == 1) {
                break;
            }
        }

        while (y_current < bound) {
            y_power.push_back(y_current);
            y_current *= y;
            if (y == 1) {
                break;
            }
        }

        set<int> result;
        for (auto& i : x_power) {
            for (auto j : y_power) {
                if (i + j <= bound) {
                    result.insert(i + j);
                }
            }
        }
        return {result.begin(), result.end()};
    }
};


int main() {
    Solution s;
    vector<tuple<tuple<int, int, int>, vector<int>>> test_cases {
        {{2, 1, 10}, {2,3,5,9}},
        {{2, 3, 10}, {2,3,4,5,7,9,10}},
        {{3, 5, 15}, {2,4,6,8,10,14}},
    };

    for (auto& test_case: test_cases) {
        assert(s.powerfulIntegers(get<0>(get<0>(test_case)), get<1>(get<0>(test_case)), get<2>(get<0>(test_case))) == get<1>(test_case));
    }
}
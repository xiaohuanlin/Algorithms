#include <vector>
#include <stack>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// There is a broken calculator that has the integer startValue on its display initially. In on operation you can:

// multiply the number on the display by 2, or
// subtract 1 from the number on the display.
// Given two integers startValue and target, return the minimum number of operations needed to display target on the calculator.

 

// Example 1:

// Input: startValue = 2, target = 3
// Output: 2
// Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.
// Example 2:

// Input: startValue = 5, target = 8
// Output: 2
// Explanation: Use decrement and then double {5 -> 4 -> 8}.
// Example 3:

// Input: startValue = 3, target = 10
// Output: 3
// Explanation: Use double, decrement and double {3 -> 6 -> 5 -> 10}.
// Example 4:

// Input: startValue = 1024, target = 1
// Output: 1023
// Explanation: Use decrement operations 1023 times.
 

// Constraints:

// 1 <= x, y <= 10^9


class Solution {
public:
    int brokenCalc(int startValue, int target) {
        int count = 0;
        while (startValue != target) {
            if (startValue > target) {
                return startValue - target + count;
            }
        
            if (target % 2 == 0) {
                target /= 2;
            } else {
                target++;
            }
            count++;
        }
        return count;
    }
};

int main() {
    Solution s;
    vector<tuple<tuple<int, int>, int>> test_cases {
        {{2, 3}, 2},
        {{5, 8}, 2},
        {{3, 10}, 3},
        {{1024, 1}, 1023},
    };

    for (auto& test_case: test_cases) {
        assert(s.brokenCalc(get<0>(get<0>(test_case)), get<1>(get<0>(test_case))) == get<1>(test_case));
    }
}
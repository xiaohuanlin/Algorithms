#include <vector>
#include <stack>
#include <iostream>
#include <tuple>
#include <assert.h>
#include <algorithm>
using namespace std;

// Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

// Example 1:

// Input: temperatures = [73,74,75,71,69,72,76,73]
// Output: [1,1,4,2,1,1,0,0]
// Example 2:

// Input: temperatures = [30,40,50,60]
// Output: [1,1,1,0]
// Example 3:

// Input: temperatures = [30,60,90]
// Output: [1,1,0]
 

// Constraints:

// 1 <= temperatures.length <= 10^5
// 30 <= temperatures[i] <= 100

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        // it is hard to know use this skill
        stack<int> candidates;
        candidates.push(temperatures.size() - 1);
        vector<int> res(temperatures.size(), 0);

        for (int i = temperatures.size() - 2; i >= 0; --i) {
            if (temperatures[i] < temperatures[candidates.top()]) {
                res[i] = candidates.top() - i;
            } else {
                while (!candidates.empty() && 
                        temperatures[i] >= temperatures[candidates.top()]) {
                    candidates.pop();
                }
                if (!candidates.empty()) {
                    res[i] = candidates.top() - i;
                }
            }
            candidates.push(i);
        }
        return res;
    }
};

int main() {
    Solution s;
    vector<tuple<vector<int>, vector<int>>> test_cases {
        {{30}, {0}},
        {{30,60,90}, {1,1,0}},
        {{30,40,50,60}, {1,1,1,0}},
        {{73,74,75,71,69,72,76,73}, {1,1,4,2,1,1,0,0}}
    };

    for (auto& test_case: test_cases) {
        assert(s.dailyTemperatures(get<0>(test_case)) == get<1>(test_case));
    }
}
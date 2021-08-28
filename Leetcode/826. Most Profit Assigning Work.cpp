#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;


// You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

// difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
// worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
// Every worker can be assigned at most one job, but one job can be completed multiple times.

// For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
// Return the maximum profit we can achieve after assigning the workers to the jobs.

 

// Example 1:

// Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
// Output: 100
// Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.
// Example 2:

// Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
// Output: 0
 

// Constraints:

// n == difficulty.length
// n == profit.length
// m == worker.length
// 1 <= n, m <= 104
// 1 <= difficulty[i], profit[i], worker[i] <= 105


class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        multimap<int, int> maps;
        for (int i = 0; i < difficulty.size(); i++) {
            maps.insert({difficulty[i], profit[i]});
        }

        int max_v = INT32_MIN;
        // calculate the max profit less than the current difficulty
        for (auto iter = maps.begin(); iter != maps.end(); iter++) {
            max_v = max(max_v, iter->second);
            iter->second = max_v;
        }

        int result = 0;
        for (auto w: worker) {
            auto iter = maps.upper_bound(w);
            if (iter != maps.begin()) {
                result += prev(iter)->second;
            }
        }
        return result;
    }
};


int main() {
    Solution s;
    vector<tuple<tuple<vector<int>, vector<int>, vector<int>>, int>> test_cases {
        {{{66,1,28,73,53,35,45,60,100,44,59,94,27,88,7,18,83,18,72,63}, 
        {66,20,84,81,56,40,37,82,53,45,43,96,67,27,12,54,98,19,47,77}, 
        {61,33,68,38,63,45,1,10,53,23,66,70,14,51,94,18,28,78,100,16}}, 1392},
        {{{68,35,52,47,86}, {67,17,1,81,3}, {92,10,85,84,82}}, 324},
        {{{2,4,6,8,10}, {10,20,30,40,50}, {4,5,6,7}}, 100},
        {{{85,47,57}, {24,66,99}, {40,25,25}}, 0},
    };

    for (auto& test_case: test_cases) {
        assert(s.maxProfitAssignment(get<0>(get<0>(test_case)), get<1>(get<0>(test_case)), get<2>(get<0>(test_case))) == get<1>(test_case));
    }
}
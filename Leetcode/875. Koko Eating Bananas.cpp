#include <vector>
#include <math.h>
#include <deque>
#include <tuple>
#include <unordered_map>
#include <assert.h>
using namespace std;

// Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

// Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

// Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

// Return the minimum integer k such that she can eat all the bananas within h hours.

 

// Example 1:

// Input: piles = [3,6,7,11], h = 8
// Output: 4
// Example 2:

// Input: piles = [30,11,23,4,20], h = 5
// Output: 30
// Example 3:

// Input: piles = [30,11,23,4,20], h = 6
// Output: 23
 

// Constraints:

// 1 <= piles.length <= 10^4
// piles.length <= h <= 10^9
// 1 <= piles[i] <= 10^9

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int start = 1;
        int end = 1;
        for (auto& pile: piles) {
            if (pile > end) {
                end = pile;
            }
        }

        while (start < end) {
            int middle = (end - start) / 2 + start;
            if (is_right(piles, middle, h)) {
                end = middle;
            } else {
                start = middle + 1;
            }
        }
        return start;
    }

    bool is_right(vector<int>& piles, int eat, int h) {
        int sum = 0;
        for (auto& pile: piles) {
            sum += (pile / eat + (pile % eat != 0));
        }
        return sum <= h;
    }
};


int main() {
    Solution s;
    vector<tuple<tuple<vector<int>, int>, int>> test_cases {
        {{{3,6,7,11}, 8}, 4},
        {{{30,11,23,4,20}, 5}, 30},
        {{{30,11,23,4,20}, 6}, 23},
    };

    for (auto& test_case: test_cases) {
        assert(s.minEatingSpeed(get<0>(get<0>(test_case)), get<1>(get<0>(test_case))) == get<1>(test_case));
    }
}
#include <vector>
#include <stack>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;


// Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

// Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

// Example 1:

// Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
// Output: true
// Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
// Example 2:

// Input: hand = [1,2,3,4,5], groupSize = 4
// Output: false
// Explanation: Alice's hand can not be rearranged into groups of 4.

 

// Constraints:

// 1 <= hand.length <= 10^4
// 0 <= hand[i] <= 10^9
// 1 <= groupSize <= hand.length
 

// Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/


class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        if (hand.size() % groupSize) {
            return false;
        }
        sort(hand.begin(), hand.end());

        // key is the last number of group, the values of stack are the size of this group
        unordered_map<int, stack<int>> maps;
        for (auto& num: hand) {
            if (maps[num - 1].empty()) {
                if (groupSize != 1) {
                    maps[num].push(1);
                }
            } else {
                int size = maps[num - 1].top() + 1;
                if (size != groupSize) {
                    maps[num].push(size);
                }
                maps[num - 1].pop();
            }

            // maybe it will save our time
            if (!maps[num - 2].empty()) {
                return false;
            }
        }

        for (auto& iter: maps) {
            if (!iter.second.empty()) {
                return false;
            }
        }
        return true;
    }
};


int main() {
    Solution s;
    vector<tuple<tuple<vector<int>, int>, bool>> test_cases {
        {{{1,2,3,6,2,3,4,7,8}, 1}, true},
        {{{1,2,3,6,2,3,4,7,8}, 3}, true},
        {{{1,2,3,4,5}, 4}, false},
    };

    for (auto& test_case: test_cases) {
        assert(s.isNStraightHand(get<0>(get<0>(test_case)), get<1>(get<0>(test_case))) == get<1>(test_case));
    }
}
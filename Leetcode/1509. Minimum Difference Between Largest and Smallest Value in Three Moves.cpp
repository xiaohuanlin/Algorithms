#include <vector>
#include <queue>
#include <stack>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// You are given a string s and two integers x and y. You can perform two types of operations any number of times.

// Remove substring "ab" and gain x points.
// For example, when removing "ab" from "cabxbae" it becomes "cxbae".
// Remove substring "ba" and gain y points.
// For example, when removing "ba" from "cabxbae" it becomes "cabxe".
// Return the maximum points you can gain after applying the above operations on s.

 

// Example 1:

// Input: s = "cdbcbbaaabab", x = 4, y = 5
// Output: 19
// Explanation:
// - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
// - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
// - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
// - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
// Total score = 5 + 4 + 5 + 5 = 19.
// Example 2:

// Input: s = "aabbaaxybbaabb", x = 5, y = 4
// Output: 20
 

// Constraints:

// 1 <= s.length <= 10^5
// 1 <= x, y <= 10^4
// s consists of lowercase English letters.

class Solution {
public:
    int minDifference(vector<int>& nums) {
        if (nums.size() < 5) {
            return 0;
        }
        sort(nums.begin(), nums.end());

        int min_value = INT32_MAX;
        // remove first three elements
        min_value = min(nums[nums.size() - 1] - nums[3], min_value);
        // remove first two elements and last element
        min_value = min(nums[nums.size() - 2] - nums[2], min_value);
        // remove first element and last two elements
        min_value = min(nums[nums.size() - 3] - nums[1], min_value);
        // remove last three elements
        min_value = min(nums[nums.size() - 4] - nums[0], min_value);
        return min_value;
    }
};


int main() {
    Solution s;
    vector<tuple<vector<int>, int>> test_cases {
        {{5,3,2,4}, 0},
        {{1,5,0,10,14}, 1},
        {{6,6,0,1,1,4,6}, 2},
        {{1,5,6,14,15}, 1},
    };

    for (auto& test_case: test_cases) {
        assert(s.minDifference(get<0>(test_case)) == get<1>(test_case));
    }
}
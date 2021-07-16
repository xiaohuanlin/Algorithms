#include <vector>
#include <tuple>
#include <unordered_map>
#include <assert.h>
using namespace std;

// Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

// You must write an algorithm that runs in O(n) time.

 

// Example 1:

// Input: nums = [100,4,200,1,3,2]
// Output: 4
// Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
// Example 2:

// Input: nums = [0,3,7,2,5,8,4,6,0,1]
// Output: 9
 

// Constraints:

// 0 <= nums.length <= 10^5
// -10^9 <= nums[i] <= 10^9

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // we use hash table to reduce the time of searching. This table record the max length
        // of every number at current situation
        unordered_map<int, int> maps;
        for (auto& num : nums) {
            auto item = maps.find(num);
            if (item == maps.end()) {
                // search its previous number and next number
                int prev = num - 1, next = num + 1;
                int prev_max = 0, next_max = 0, cur_max;
                auto prev_iter = maps.find(prev);
                if (prev_iter != maps.end()) {
                    prev_max = prev_iter->second;
                }
                auto next_iter = maps.find(next);
                if (next_iter != maps.end()) {
                    next_max = next_iter->second;
                }

                maps[num] = cur_max = prev_max + next_max + 1;
                if (prev_iter != maps.end()) {
                    // update the first element of the previous array
                    maps[num - prev_max] = cur_max;
                }
                if (next_iter != maps.end()) {
                    // update the last element of the next array
                    maps[num + next_max] = cur_max;
                }
            }
        }

        int max_value = 0;
        for (auto& pair : maps) {
            max_value = max(max_value, pair.second);
        }
        return max_value;
    }
};

int main() {
    Solution s;
    vector<tuple<vector<int>, int>> test_cases {
        {{}, 0},
        {{5, 9, 7, 8, 6}, 5},
        {{100, 4, 200, 1, 3, 2}, 4},
        {{0, 3, 7, 2, 5, 8, 4, 6, 0, 1}, 9},
    };

    for (auto& test_case: test_cases) {
        assert(s.longestConsecutive(get<0>(test_case)) == get<1>(test_case));
    }
}
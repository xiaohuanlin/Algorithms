#include <unordered_set>
#include <unordered_map>
#include <math.h>
#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;


// Given a sorted integer array without duplicates, return the summary of its ranges.

// Example 1:

// Input:  [0,1,2,4,5,7]
// Output: ["0->2","4->5","7"]
// Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
// Example 2:

// Input:  [0,2,3,4,6,8,9]
// Output: ["0","2->4","6","8->9"]
// Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.

class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> res;
        if (nums.empty()) {
            return res;
        }

        int count = 1;
        int start = 0;
        int64_t expect = nums[0] + 1;

        while (count < nums.size()) {
            if (nums[count] != expect) {
                if (count - start > 1) {
                    res.push_back(to_string(nums[start]) + "->" + to_string(nums[count-1]));
                } else {
                    res.push_back(to_string(nums[count-1]));
                }
                start = count;
                expect = int64_t(nums[count]) + 1;
            } else {
                expect++;
            }
            count++;
        }

        if (count - start > 1) {
            res.push_back(to_string(nums[start]) + "->" + to_string(nums[count-1]));
        } else {
            res.push_back(to_string(nums[count-1]));
        }
        return res;
    }
};

int main() {
    Solution s;
    vector<int> array = {
        0,1,2,4,5,7,8
    };
    auto res = s.summaryRanges(array);
    for (auto e: res) {
        cout << e << ',';
    }
    cout << endl;
}
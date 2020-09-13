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


// Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

// You may assume the array's length is at most 10,000.

// Example:

// Input:
// [1,2,3]

// Output:
// 2

// Explanation:
// Only two moves are needed (remember each move increments or decrements one element):

// [1,2,3]  =>  [2,2,3]  =>  [2,2,2]


class Solution {
public:
    int minMoves2(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        return calcu(nums, nums[nums.size() / 2]);
    }

    int calcu(vector<int>& nums, int target){
        int res = 0;
        for (auto num: nums) {
            res += abs(target - num);
        }
        return res;
    }
};

int main() {
    Solution s;
    vector<int> array {1};
    cout << s.minMoves2(array);
}
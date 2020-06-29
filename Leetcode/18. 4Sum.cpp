#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;
// Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

// Note:

// The solution set must not contain duplicate quadruplets.

// Example:

// Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

// A solution set is:
// [
//   [-1,  0, 0, 1],
//   [-2, -1, 1, 2],
//   [-2,  0, 0, 2]
// ]
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        int size = nums.size();
        if (size < 4) {
            return res; 
        }
        int first;
        int second;

        for (first = 0; first < size - 3; first++) {
            if (first > 0 && nums[first] == nums[first-1]) 
                continue;
            // juage if the remain array will less than target
            if (nums[first] + nums[first+1] + nums[first+2] + nums[first+3] > target)
                break;
            if (nums[first] + nums[size-1] + nums[size-2] + nums[size-3] < target)
                continue;

            for (second = first + 1; second < size - 2; second ++) {
                if (second > first+1 && nums[second] == nums[second-1]) 
                    continue;
                // juage if the remain array will less than target
                if (nums[first] + nums[second] + nums[second+1] + nums[second+2] > target)
                    break;
                if (nums[first] + nums[second] + nums[size-1] + nums[size-2] < target)
                    continue;

                int left = second + 1;
                int right = size - 1;
                while (left < right) {
                    if (nums[first] + nums[second] + nums[left] + nums[right] > target) {
                        right--;
                    } else if (nums[first] + nums[second] + nums[left] + nums[right] == target) {
                        vector<int> unit = {nums[first], nums[second], nums[left], nums[right]};
                        res.push_back(unit);
                        int now_left = nums[left];
                        while (left < right && nums[left] == now_left) {
                            left++;
                        }
                        int now_right= nums[right];
                        while (left < right && nums[right] == now_right) {
                            right--;
                        }
                    } else {
                        left++;
                    }
                }
            }
        }

        return res;
    }
};


int main() {
    Solution s;
    vector<int> array1 = {-5, -4, -3,-2,-1,0,0,1,2,3, 4, 5};
    auto res = s.fourSum(array1, 0);

    for (auto e: res) {
        for (auto l: e) {
            cout << l << ',';
        }
        cout << endl;
    }
    cout << endl;
}
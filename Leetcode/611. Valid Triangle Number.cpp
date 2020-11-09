#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
#include <unordered_map>
using namespace std;


// Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
// Example 1:
// Input: [2,2,3,4]
// Output: 3
// Explanation:
// Valid combinations are: 
// 2,3,4 (using the first 2)
// 2,3,4 (using the second 2)
// 2,2,3
// Note:
// The length of the given array won't exceed 1000.
// The integers in the given array are in the range of [0, 1000].


class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int16_t> counts(1001, -1);
        // the last index of value 
        for (int i = 0; i < nums.size(); i++) {
            counts[nums[i]] = i;
        }

        int16_t prev = -1;
        for (int i = 0; i < 1001; i++) {
            if (counts[i] == -1) {
                counts[i] = prev;
            } else {
                prev = counts[i];
            }
        }

        int result = 0;
        for (int i = counts[0] + 1; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                int low = j;
                int high = counts[min(max(nums[j] + nums[i] - 1, 0), 1000)];
                result += high - low;
            }
        }
        return result;
    }
};

int main() {
    Solution s;
    vector<int> array {2,2,3,4};
    cout << s.triangleNumber(array);
}
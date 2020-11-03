#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;


// You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

// Follow up: Your solution should run in O(log n) time and O(1) space.

 

// Example 1:

// Input: nums = [1,1,2,3,3,4,4,8,8]
// Output: 2
// Example 2:

// Input: nums = [3,3,7,7,10,11,11]
// Output: 10
 

// Constraints:

// 1 <= nums.length <= 10^5
// 0 <= nums[i] <= 10^5


class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int start = 0;
        int end = nums.size() - 1;
        while (start < end) {
            int middle = start + (end - start) / 2;
            middle = middle % 2 ? middle: middle + 1;

            if (nums[middle] == nums[middle-1]) {
                start = middle + 1;
            } else {
                if (nums[middle] == nums[middle+1]) {
                    end = middle - 1;
                } else {
                    return middle;
                }
            }
        }
        return nums[start];
    }
};

int main() {
    Solution s;
    vector<int> array {1, 2, 2};
    cout << s.singleNonDuplicate(array);
}
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

// If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

// The replacement must be in-place and use only constant extra memory.

// Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

// 1,2,3 → 1,3,2
// 3,2,1 → 1,2,3
// 1,1,5 → 1,5,1

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        if (nums.size() <= 1) {
            return;
        }

        int exchange_index = nums.size() - 2;
        while (exchange_index >= 0 && nums[exchange_index] >= nums[exchange_index+1]) {
            exchange_index --;
        }

        int middle = 0;

        if (exchange_index >= 0) {

            // find larger than exchange value
            int left = exchange_index + 1;
            int right = nums.size() - 1;
            middle = left + (right - left) / 2;
            while (left < right) {
                if (nums[middle] > nums[exchange_index]) {
                    left = middle + 1;
                } else if (nums[middle] <= nums[exchange_index]) {
                    right = middle - 1;
                }
                middle = left + (right - left) / 2;
            }

            if (nums[middle] <= nums[exchange_index]) {
                middle--;
            }

            // swap two value
            int tmp = nums[middle];
            nums[middle] = nums[exchange_index];
            nums[exchange_index] = tmp;

        }

        // sort
        sort(nums.begin() + exchange_index + 1, nums.end());
    }
};


int main() {
    Solution s;
    vector<int> array = {5,1,1};
    s.nextPermutation(array);
    for (auto e: array) {
        cout << e << ',';
    }
    cout << endl;
}
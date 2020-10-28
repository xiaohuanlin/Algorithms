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

// Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

// Example 1:
// Input: [1,2,1]
// Output: [2,-1,2]
// Explanation: The first 1's next greater number is 2; 
// The number 2 can't find next greater number; 
// The second 1's next greater number needs to search circularly, which is also 2

class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        if (nums.empty()) {
            return {};
        }
        if (nums.size() == 1) {
            return {-1};
        }

        deque<int> compare {0};
        vector<int> result(nums.size(), INT32_MIN);

        int count = 1;
        while (!compare.empty()) {

            if (count == compare.front()) {
                // Though we search whole list, we can't find answer
                result[count] = -1;
                compare.pop_front();
            }

            while (!compare.empty() && nums[compare.back()] < nums[count]) {
                // we find grater number
                result[compare.back()] = nums[count];
                compare.pop_back();
            }

            if (result[count] == INT32_MIN) {
                // we don't calculate this reuslt, so push it into deque
                compare.push_back(count);
            }

            count++;
            count %= nums.size();
        }
        return result;
    }
};


int main() {
    Solution s;
    vector<int> array {1, 2, 1};
    auto res = s.nextGreaterElements(array);
    for (auto e: res) {
        cout << e << ',';
    }
}
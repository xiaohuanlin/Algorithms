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


// Given a list of positive integers, the adjacent integers will perform the float division. For example, [2,3,4] -> 2 / 3 / 4.

// However, you can add any number of parenthesis at any position to change the priority of operations. You should find out how to add parenthesis to get the maximum result, and return the corresponding expression in string format. Your expression should NOT contain redundant parenthesis.

// Example:
// Input: [1000,100,10,2]
// Output: "1000/(100/10/2)"
// Explanation:
// 1000/(100/10/2) = 1000/((100/10)/2) = 200
// However, the bold parenthesis in "1000/((100/10)/2)" are redundant, 
// since they don't influence the operation priority. So you should return "1000/(100/10/2)". 

// Other cases:
// 1000/(100/10)/2 = 50
// 1000/(100/(10/2)) = 50
// 1000/100/10/2 = 0.5
// 1000/100/(10/2) = 2
// Note:

// The length of the input array is [1, 10].
// Elements in the given array will be in range [2, 1000].
// There is only one optimal division for each test case.


class Solution {
public:
    string optimalDivision(vector<int>& nums) {
        if (nums.size() == 1) {
            return to_string(nums[0]);
        }
        string res = to_string(nums[0]) + '/';
        int size = nums.size();
        if (size != 2) {
            res += '(';
        }
        for (int i = 1; i < size; i++) {
            res += to_string(nums[i]);
            if (i != size - 1) {
                res += '/';
            }
        }
        if (size != 2) {
            res += ')';
        }
        return res;
    }
};


int main() {
    Solution s;
    vector<int> array {1000, 100, 10, 2};
    cout << s.optimalDivision(array);
}
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


// sentation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
// showing the four bits relevant in this case). So the answer will be:
// HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
// Note:
// Elements of the given array are in the range of 0 to 10^9
// Length of the array will not exceed 10^4.


class Solution {

public:
    int totalHammingDistance(vector<int>& nums) {
        // you should use matrix as an array
        int total = 0;
        for (int j = 0; j < 32; ++j) {
            int one_count = 0;
            int zero_count = 0;
            for (int i = 0; i < nums.size(); ++i) {
                if (nums[i] & 1) {
                    ++one_count;
                } else {
                    ++zero_count;
                }
                nums[i] >>= 1;
            }

            total += one_count * zero_count;
        }
        return total;
    }

};


int main() {
    Solution s;
    vector<int> array {4, 14, 2};
    cout << s.totalHammingDistance(array);
}
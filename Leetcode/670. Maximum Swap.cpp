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


// Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

// Example 1:
// Input: 2736
// Output: 7236
// Explanation: Swap the number 2 and the number 7.
// Example 2:
// Input: 9973
// Output: 9973
// Explanation: No swap.
// Note:
// The given number is in the range [0, 108]

class Solution {
public:
    int maximumSwap(int num) {
        auto num_array = to_array(num);

        vector<int> max_idx_array;
        int max_v = INT32_MIN;
        int max_idx = -1;
        for (int i = num_array.size() - 1; i >= 0; --i) {
            if (num_array[i] > max_v) {
                max_v = num_array[i];
                max_idx = i;
            }
            max_idx_array.push_back(max_idx);
        }
        reverse(max_idx_array.begin(), max_idx_array.end());

        for (int i = 0; i < num_array.size() - 1; ++i) {
            int max_idx = max_idx_array[i+1];
            if (num_array[i] < num_array[max_idx]) {
                swap(num_array[i], num_array[max_idx]);
                return to_num(num_array);
            }
        }
        return num;
    }

    vector<int> to_array(int num) {
        vector<int> res;
        while (num) {
            res.push_back(num % 10);
            num /= 10;
        }
        reverse(res.begin(), res.end());
        if (res.empty()) {
            res.push_back(0);
        }
        return res;
    }

    int to_num(vector<int> &array) {
        int result = 0;
        for (auto &e: array) {
            result = 10 * result + e;    
        }
        return result;
    }
};


int main() {
}
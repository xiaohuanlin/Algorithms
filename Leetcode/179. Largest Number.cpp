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


// Given a list of non negative integers, arrange them such that they form the largest number.

// Example 1:

// Input: [10,2]
// Output: "210"
// Example 2:

// Input: [3,30,34,5,9]
// Output: "9534330"
// Note: The result may be very large, so you need to return a string instead of an integer.

class Solution {
public:
    string largestNumber(vector<int>& nums) {
        vector<string> res;
        for (int i = 0; i < nums.size(); i++) {
            res.push_back(to_string(nums[i]));
        }

        sort(res.begin(), res.end(), [](const string &a, const string &b){return a+b > b+a;});
        
        string res_word;
        bool has_zero = false;
        for (int i = 0; i < res.size(); i++) {
            if (!has_zero && res[i] == "0") {
                continue;
            }

            has_zero = true;
            res_word += res[i];
        }
        if (res_word.empty()) {
            return "0";
        }
        return res_word;
    }

};


int main() {
    Solution s;
    vector<int> array = {
        0,0,0,0,12,23
    };
    cout << s.largestNumber(array);
}
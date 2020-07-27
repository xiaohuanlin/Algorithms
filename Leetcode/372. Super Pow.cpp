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


// Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

// Example 1:

// Input: a = 2, b = [3]
// Output: 8
// Example 2:

// Input: a = 2, b = [1,0]
// Output: 1024

class Solution {
public:
    int superPow(int a, vector<int>& b) {
        bool all_zero = false;
        int pre_multi = a % 1337;
        int multi = 1;
        while (!all_zero) {
            if (divide_two(b, all_zero) == 1) {
                multi = (multi * pre_multi) % 1337;
            }
            pre_multi = (pre_multi * pre_multi) % 1337;
        }
        return multi;
    }

    int divide_two(vector<int> &num, bool &all_zero) {
        int count = 0;
        int carry = 0;
        all_zero = true;
        while (count < num.size()) {
            int tmp = num[count];
            num[count] = ((tmp + carry * 10) / 2);
            if (num[count] != 0) {
                all_zero = false;
            }
            carry = (tmp + carry * 10) % 2;
            count++;
        }

        return carry;
    }
};

int main() {
    Solution s;
    vector<int> array = {8};
    cout << s.superPow(3, array);
}
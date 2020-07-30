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
#include <queue>
using namespace std;

// Given an integer n, return 1 - n in lexicographical order.

// For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

// Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.


class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> res;
        backtrace(res, 0, n);
        res.erase(res.begin());
        return res;
    }

    void backtrace(vector<int> &res, int value, int limit) {
        res.push_back(value);

        int base_value = value * 10;
        for (int i = 0; i < 10; i++) {
            if (base_value == 0 && i == 0) {
                continue;
            }
            if (base_value + i <= limit) {
                backtrace(res, base_value + i, limit);
            }
        }
    }
};


int main() {
    Solution s;
    auto res = s.lexicalOrder(13);
    for (auto e: res) {
        cout << e << ',';
    }
    cout << endl;
}

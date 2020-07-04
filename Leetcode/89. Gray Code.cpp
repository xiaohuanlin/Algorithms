#include <math.h>
#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// The gray code is a binary numeral system where two successive values differ in only one bit.

// Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

// Example 1:

// Input: 2
// Output: [0,1,3,2]
// Explanation:
// 00 - 0
// 01 - 1
// 11 - 3
// 10 - 2

// For a given n, a gray code sequence may not be uniquely defined.
// For example, [0,2,3,1] is also a valid gray code sequence.

// 00 - 0
// 10 - 2
// 11 - 3
// 01 - 1
// Example 2:

// Input: 0
// Output: [0]
// Explanation: We define the gray code sequence to begin with 0.
//              A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
//              Therefore, for n = 0 the gray code sequence is [0].

class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> res = {0};
        set<int> path = {0};
        getGreyCode(res, path, 0, n, pow(2, n));
        return res;
    }

    void getGreyCode(vector<int> &res, set<int> &path, int previous, int n, int target) {
        if (res.size() == target) {
            return;
        }

        int current;
        for (int i = 0; i < n; i++) {
            current = previous ^ (1 << i);
            if (path.find(current) != path.end()) {
                continue;
            }
            res.push_back(current);
            path.insert(current);
            getGreyCode(res, path, current, n, target);
        }
    }


    vector<int> grayCodeNew(int n) {
        vector<int> res = {0};
        int count = 0;
        while (count < n) {
            for (int i = res.size() - 1; i >= 0; i--) {
                res.push_back(res[i] ^ (1 << count));
            }
            count ++;
        }
        return res;
    }
};

int main() {
    Solution s;
    auto res = s.grayCodeNew(3);
    for (auto e: res) {
        cout << e << ',';
    }
    cout << endl;
}
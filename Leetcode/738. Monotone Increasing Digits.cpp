#include <vector>
#include <stack>
#include <iostream>
#include <tuple>
#include <assert.h>
#include <algorithm>
using namespace std;

// An integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.

// Given an integer n, return the largest number that is less than or equal to n with monotone increasing digits.

 

// Example 1:

// Input: n = 10
// Output: 9
// Example 2:

// Input: n = 1234
// Output: 1234
// Example 3:

// Input: n = 332
// Output: 299
 

// Constraints:

// 0 <= n <= 10^9


class Solution {
public:
    int monotoneIncreasingDigits(int n) {
        if (n < 10) {
            return n;
        }

        vector<int> number, res;
        intToVector(number, n);
        int left_max = number.front();
        vector<int> sep(number.size(), left_max);

        res.push_back(left_max);
        // less then "iiiiii"
        if (n < vectorToInt(sep.begin(), sep.end())) {
            for (int i = 1; i < number.size(); ++i) {
                res.push_back(0);
            }
            return vectorToInt(res.begin(), res.end()) - 1;
        }

        int remain = monotoneIncreasingDigits(vectorToInt(number.begin() + 1, number.end()));
        return stoi(to_string(left_max)+ to_string(remain));
    }

    void intToVector(vector<int>& res, int n) {
        if (n == 0) {
            res.push_back(0);
            return;
        }

        while (n) {
            res.push_back(n % 10);
            n /= 10;
        }
        int start = 0, end = res.size() - 1;
        while (start < end) {
            swap(res[start++], res[end--]);
        }
        return;
    }

    int vectorToInt(vector<int>::iterator begin, vector<int>::iterator end) {
        int res = 0;
        while (begin != end) {
            res = res * 10 + *begin;
            ++begin;
        }
        return res;
    }
};

int main() {
    Solution s;
    vector<tuple<int, int>> test_cases {
        {101, 99},
        {100, 99},
        {0, 0},
        {10, 9},
        {1234, 1234},
        {332, 299},
        {2322, 2299},
        {2415, 2399},
        {399443, 389999},
    };

    for (auto& test_case: test_cases) {
        assert(s.monotoneIncreasingDigits(get<0>(test_case)) == get<1>(test_case));
    }
}
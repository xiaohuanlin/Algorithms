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


// Write a program to find the n-th ugly number.

// Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

// Example:

// Input: n = 10
// Output: 12
// Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
// Note:  

// 1 is typically treated as an ugly number.
// n does not exceed 1690.


class Solution {
public:
    int nthUglyNumber(int n) {
        int two_point = 0;
        int three_point = 0;
        int five_point = 0;
        vector<int> res = {1};
        while (res.size() < n) {
            int two = res[two_point] * 2;
            int three = res[three_point] * 3;
            int five = res[five_point] * 5;
            int tmp = min(min(two, three), five);
            if (tmp == two) {
                two_point++;
            } else if (tmp == three) {
                three_point++;
            } else {
                five_point++;
            }
            
            if (tmp != res.back()) {
                res.push_back(tmp);
            }
        }

        return res.back();
    }
};


int main() {
    Solution s;
    cout << s.nthUglyNumber(10);
}

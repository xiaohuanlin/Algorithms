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


// Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

// Example:

// Input: 2
// Output: 91 
// Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
//              excluding 11,22,33,44,55,66,77,88,99
 

// Constraints:

// 0 <= n <= 8

class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        int before = 0;
        int count = 0;
        while (count <= n) {
            int multi = 1;
            for (int i = 0; i < count; i++) {
                if (i == 0) {
                    multi = 9;
                } else {
                    multi *= (10 - i); 
                }
            }
            before += multi;
            count++;
        }
        return before;
    }
};

int main() {
    Solution s;
    cout << s.countNumbersWithUniqueDigits(3);
}
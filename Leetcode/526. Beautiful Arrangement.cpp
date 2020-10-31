#include <unordered_map>
#include <unordered_set>
#include <math.h>
#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;


// Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

// The number at the ith position is divisible by i.
// i is divisible by the number at the ith position.
 

// Now given N, how many beautiful arrangements can you construct?

// Example 1:

// Input: 2
// Output: 2
// Explanation: 

// The first beautiful arrangement is [1, 2]:

// Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

// Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

// The second beautiful arrangement is [2, 1]:

// Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

// Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
 

// Note:

// N is a positive integer and will not exceed 15.


class Solution {
public:
    int countArrangement(int N) {
        vector<int> candidate(N, 0);
        for (int i = 1; i < N + 1; i++) {
            candidate[i-1] = i;
        }
        int result = 0;
        backtrace(candidate, 1, result);
        return result;
    }

    void backtrace(vector<int> &candidate, int index, int &result) {
        if (candidate.empty()) {
            result++;
            return;
        }

        for (int i = 0; i < candidate.size(); i++) {
            int value = candidate[i];
            if (value % index == 0 || index % value == 0) {
                candidate.erase(candidate.begin() + i);
                backtrace(candidate, index + 1, result);
                candidate.insert(candidate.begin() + i, value);
            }
        }

    }
};


int main() {
    Solution s;
    cout << s.countArrangement(3) << endl;
}
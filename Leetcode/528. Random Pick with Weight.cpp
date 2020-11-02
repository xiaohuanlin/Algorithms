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


// You are given an array of positive integers w where w[i] describes the weight of ith index (0-indexed).

// We need to call the function pickIndex() which randomly returns an integer in the range [0, w.length - 1]. pickIndex() should return the integer proportional to its weight in the w array. For example, for w = [1, 3], the probability of picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).

// More formally, the probability of picking index i is w[i] / sum(w).

 

// Example 1:

// Input
// ["Solution","pickIndex"]
// [[[1]],[]]
// Output
// [null,0]

// Explanation
// Solution solution = new Solution([1]);
// solution.pickIndex(); // return 0. Since there is only one single element on the array the only option is to return the first element.
// Example 2:

// Input
// ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
// [[[1,3]],[],[],[],[],[]]
// Output
// [null,1,1,1,1,0]

// Explanation
// Solution solution = new Solution([1, 3]);
// solution.pickIndex(); // return 1. It's returning the second element (index = 1) that has probability of 3/4.
// solution.pickIndex(); // return 1
// solution.pickIndex(); // return 1
// solution.pickIndex(); // return 1
// solution.pickIndex(); // return 0. It's returning the first element (index = 0) that has probability of 1/4.

// Since this is a randomization problem, multiple answers are allowed so the following outputs can be considered correct :
// [null,1,1,1,1,0]
// [null,1,1,1,1,1]
// [null,1,1,1,0,0]
// [null,1,1,1,0,1]
// [null,1,0,1,0,0]
// ......
// and so on.
 

// Constraints:

// 1 <= w.length <= 10000
// 1 <= w[i] <= 10^5
// pickIndex will be called at most 10000 times.

class Solution {
    int sum;
    vector<pair<int, int>> bounds;
public:
    Solution(vector<int>& w) {
        sum = 0;
        for (int i = 0; i < w.size(); i++) {
            bounds.push_back({sum, sum+w[i]});
            sum += w[i];
        }
    }
    
    int pickIndex() {
        int rand_v = rand() % sum;
        // find bounds by log2index
        cout << "get rand " << rand_v << endl;

        int start = 0;
        int end = bounds.size();
        while (start < end) {
            int middle = start + (end - start) / 2;
            if (rand_v < bounds[middle].first) {
                end = middle - 1;
            } else if (rand_v >= bounds[middle].second) {
                start = middle + 1;
            } else {
                return middle;
            }
        }
        return start;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */

int main() {
    vector<int> array {3, 14, 1, 7};
    Solution s(array);
    cout << s.pickIndex() << endl;
    cout << s.pickIndex() << endl;
    cout << s.pickIndex() << endl;
    cout << s.pickIndex() << endl;
    cout << s.pickIndex() << endl;
    cout << s.pickIndex() << endl;
    cout << s.pickIndex() << endl;
    cout << s.pickIndex() << endl;
    cout << s.pickIndex() << endl;
    cout << s.pickIndex() << endl;
    cout << s.pickIndex() << endl;
    cout << s.pickIndex() << endl;
    cout << s.pickIndex() << endl;
    cout << s.pickIndex() << endl;
    cout << s.pickIndex() << endl;
    cout << s.pickIndex() << endl;
    cout << s.pickIndex() << endl;
    cout << s.pickIndex() << endl;
}
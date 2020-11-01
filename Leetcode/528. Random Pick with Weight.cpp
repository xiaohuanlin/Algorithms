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
    int all_sum;
    vector<int> bounds;
    vector<int> log2index;
public:
    Solution(vector<int>& w) {
        int sum = 0;
        for (int i = 0; i < w.size(); i++) {
            sum += w[i];
            bounds.push_back(sum);
        }
        all_sum = sum;

        // build a list tell the according num bound of 2^x
        // bounds: [1, 5, 9]
        // log2: 2^0, 2^1, 2^2, 2^3 
        // log2index: [0, 1, 1, 2]
        int max_v = int(log2(sum)) + 1;
        int j = 0;
        log2index.push_back(0);
        for (int i = 0; i < max_v; i++) {
            int found_v = (1 << i);
            while (found_v >= bounds[j]) {
                j++;
            }
            log2index.push_back(j);
        }
    }
    
    int pickIndex() {
        int rand_v = rand() % all_sum;
        // cout << "get rand_v: " << rand_v << endl;
        // find bounds by log2index
        int max_v = int(log2index.size() - 1);
        int log_min = 0;
        if (rand_v) {
            log_min = min(int(log2(rand_v)) + 1, max_v);
        }
        int log_max = min(log_min + 1, max_v);

        for (int start = log2index[log_min]; start <= log2index[log_max]; start++) {
            if (rand_v < bounds[start]) {
                return start;
            }
        }
        return -1;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */

int main() {
    vector<int> array {1, 3, 1};
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
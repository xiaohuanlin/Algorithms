#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// The set [1,2,3,...,n] contains a total of n! unique permutations.

// By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

// "123"
// "132"
// "213"
// "231"
// "312"
// "321"
// Given n and k, return the kth permutation sequence.

// Note:

// Given n will be between 1 and 9 inclusive.
// Given k will be between 1 and n! inclusive.
// Example 1:

// Input: n = 3, k = 3
// Output: "213"
// Example 2:

// Input: n = 4, k = 9
// Output: "2314"

class Solution {
public:
    string getPermutation(int n, int k) {
        string res(n, '0');
        vector<char> candidates;
        for (int i = 0; i < n; i++) {
            candidates.push_back(i + '1');
        }
        vector<int> unit_nums(n, 1);
        for (int i = 1; i < n; i++) {
            unit_nums[i] = unit_nums[i-1] * i;
        }
        if (n * unit_nums[n-1] < k) {
            res.resize(0);
            return res; 
        }

        k --;
        for (int i = 0; i < n; i++) {
            int cur_unit_num = unit_nums[n - i - 1];
            int candidate_index = k / cur_unit_num;
            k %= cur_unit_num;
            res[i] = candidates[candidate_index];
            candidates.erase(candidates.begin() + candidate_index);
        }
        return res;
    }
};

int main() {
    Solution s;
    auto res = s.getPermutation(3, 2);
    cout << res;
}

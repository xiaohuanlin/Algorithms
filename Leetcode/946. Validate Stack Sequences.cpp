#include <vector>
#include <stack>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;


// Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

 

// Example 1:

// Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
// Output: true
// Explanation: We might do the following sequence:
// push(1), push(2), push(3), push(4),
// pop() -> 4,
// push(5),
// pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
// Example 2:

// Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
// Output: false
// Explanation: 1 cannot be popped before 2.
 

// Constraints:

// 1 <= pushed.length <= 1000
// 0 <= pushed[i] <= 1000
// All the elements of pushed are unique.
// popped.length == pushed.length
// popped is a permutation of pushed.


class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        if (pushed.size() != popped.size()) {
            return false;
        }
        if (pushed.size() == 0) {
            return true;
        }

        stack<int> res;
        res.push(pushed[0]);
        auto push_iter = pushed.begin() + 1;
        auto pop_iter = popped.begin();
        do {
            // enter stack
            while (push_iter != pushed.end() && (res.empty() || res.top() != *pop_iter)) {
                res.push(*push_iter);
                push_iter++;
            }

            // quit stack
            while (pop_iter != popped.end() && !res.empty() && res.top() == *pop_iter) {
                res.pop();
                pop_iter++;
            }
        } while (push_iter != pushed.end() && pop_iter != popped.end());
        return push_iter == pushed.end() && pop_iter == popped.end();
    }
};


int main() {
    Solution s;
    vector<tuple<tuple<vector<int>, vector<int>>, bool>> test_cases {
        {{{1,0}, {1,0}}, true},
        {{{0}, {0}}, true},
        {{{1,2,3,4,5}, {4,5,3,2,1}}, true},
        {{{1,2,3,4,5}, {4,3,5,1,2}}, false},
    };

    for (auto& test_case: test_cases) {
        assert(s.validateStackSequences(get<0>(get<0>(test_case)), get<1>(get<0>(test_case))) == get<1>(test_case));
    }
}
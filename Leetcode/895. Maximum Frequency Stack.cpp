#include <vector>
#include <stack>
#include <unordered_map>
#include <set>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;


// Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

// Implement the FreqStack class:

// FreqStack() constructs an empty frequency stack.
// void push(int val) pushes an integer val onto the top of the stack.
// int pop() removes and returns the most frequent element in the stack.
// If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
 

// Example 1:

// Input
// ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
// [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
// Output
// [null, null, null, null, null, null, null, 5, 7, 5, 4]

// Explanation
// FreqStack freqStack = new FreqStack();
// freqStack.push(5); // The stack is [5]
// freqStack.push(7); // The stack is [5,7]
// freqStack.push(5); // The stack is [5,7,5]
// freqStack.push(7); // The stack is [5,7,5,7]
// freqStack.push(4); // The stack is [5,7,5,7,4]
// freqStack.push(5); // The stack is [5,7,5,7,4,5]
// freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
// freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
// freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
// freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
 

// Constraints:

// 0 <= val <= 10^9
// At most 2 * 10^4 calls will be made to push and pop.
// It is guaranteed that there will be at least one element in the stack before calling pop.


class FreqStack {
    unordered_map<int, int> key_to_freq_;
    unordered_map<int, vector<int>> freq_to_keys_;
    vector<int> store_;
    int max_freq_ = 0;
public:
    FreqStack() {}

    void push(int val) {
        int& frequence = key_to_freq_[val];
        auto& keys = freq_to_keys_[frequence];
        auto iter = find(keys.begin(), keys.end(), val);
        if (iter != keys.end()) {
            // raise to new frequence vector
            keys.erase(iter);
        }

        freq_to_keys_[++frequence].push_back(val);
        max_freq_ = max(max_freq_, frequence);
        store_.push_back(val);
    }
    
    int pop() {
        auto iter = store_.end() - 1;

        int count = 0;
        int total = store_.size();
        while (count++ < total && key_to_freq_[*iter] < max_freq_) {
            iter--;
        }

        auto& keys = freq_to_keys_[max_freq_];
        if (keys.size() == 1) {
            // remove it
            int key = *iter;
            max_freq_--;

            key_to_freq_[key]--;

            keys.pop_back();
            freq_to_keys_[key_to_freq_[key]].push_back(key);

            store_.erase(iter);
            return key;
        } else {
            int key = *iter;

            key_to_freq_[key]--;

            auto key_iter = find(keys.begin(), keys.end(), key);
            keys.erase(key_iter);

            freq_to_keys_[key_to_freq_[key]].push_back(key);

            store_.erase(iter);
            return key;
        }
    }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(val);
 * int param_2 = obj->pop();
 */


int main() {
    FreqStack* obj = new FreqStack();
    obj->push(5); // The stack is [5]
    obj->push(7); // The stack is [5,7]
    obj->push(5); // The stack is [5,7,5]
    obj->push(7); // The stack is [5,7,5,7]
    obj->push(4); // The stack is [5,7,5,7,4]
    obj->push(5); // The stack is [5,7,5,7,4,5]
    assert(obj->pop() == 5);   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
    assert(obj->pop() == 7);   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
    assert(obj->pop() == 5);   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
    assert(obj->pop() == 4);   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
}
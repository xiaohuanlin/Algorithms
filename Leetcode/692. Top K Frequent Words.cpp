#include <unordered_set>
#include <unordered_map>
#include <math.h>
#include <utility>
#include <stack>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Given a non-empty list of words, return the k most frequent elements.

// Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

// Example 1:
// Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
// Output: ["i", "love"]
// Explanation: "i" and "love" are the two most frequent words.
//     Note that "i" comes before "love" due to a lower alphabetical order.
// Example 2:
// Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
// Output: ["the", "is", "sunny", "day"]
// Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
//     with the number of occurrence being 4, 3, 2 and 1 respectively.
// Note:
// You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
// Input words contain only lowercase letters.
// Follow up:
// Try to solve it in O(n log k) time and O(n) extra space.


class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> res;
        for (auto &e: words) {
            res[e]++;
        }
        auto compare = [] (pair<int, string> left, pair<int, string> right) {
            if (left.first != right.first) {
                return left.first < right.first;
            }

            return left.second > right.second;
        };

        priority_queue<pair<int, string>, vector<pair<int, string>>, decltype(compare)> my_queue(compare);

        for (auto iter = res.begin(); iter != res.end(); iter++) {
            my_queue.push({iter->second, iter->first});
        }

        vector<string> ret;
        for (int i = 0; i < k; i++) {
            ret.push_back(my_queue.top().second);
            my_queue.pop();
        }
        return ret;
    }
};


int main() {
    Solution s;
    vector<string> array {"i", "love", "leetcode", "i", "love", "coding"};
    auto res = s.topKFrequent(array, 2);
    for (auto &e: res) {
        cout << e << ',';
    }
    cout << endl;
}
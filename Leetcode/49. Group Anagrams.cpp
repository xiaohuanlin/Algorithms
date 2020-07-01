#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Given an array of strings, group anagrams together.

// Example:

// Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
// Output:
// [
//   ["ate","eat","tea"],
//   ["nat","tan"],
//   ["bat"]
// ]
// Note:

// All inputs will be in lowercase.
// The order of your output does not matter.

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<vector<int>, vector<string>> res;
        for (int i = 0; i < strs.size(); i++) {
            vector<int> words(26, 0);
            for (int k = 0; k < strs[i].size(); k++) {
                words[strs[i][k] - 'a'] ++;
            }

            if (res.find(words) == res.end()) {
                res[words] = vector<string>(1, strs[i]);
            } else {
                res[words].push_back(strs[i]);
            }
        }
        
        vector<vector<string>> result;
        for (auto i = res.begin(); i != res.end(); i++) {
            result.push_back(i->second);
        }
        return result;
    }
};

int main() {
    Solution s;
    vector<string> words = {};
    auto res = s.groupAnagrams(words);
    for (auto e: res) {
        for (auto l: e) {
            cout << l << ',';
        }
        cout << endl;
    }
}

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


// Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

// Note:

// The same word in the dictionary may be reused multiple times in the segmentation.
// You may assume the dictionary does not contain duplicate words.
// Example 1:

// Input: s = "leetcode", wordDict = ["leet", "code"]
// Output: true
// Explanation: Return true because "leetcode" can be segmented as "leet code".
// Example 2:

// Input: s = "applepenapple", wordDict = ["apple", "pen"]
// Output: true
// Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
//              Note that you are allowed to reuse a dictionary word.
// Example 3:

// Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
// Output: false



class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_map<char, vector<string>> dict;
        for (int i = 0; i < wordDict.size(); i++) {
            if (wordDict[i] == "") {
                continue;
            }
            char word = wordDict[i][0];
            if (dict.find(word) == dict.end()) {
                dict[word] = vector<string>();
            }
            dict[word].push_back(wordDict[i]);
        }
        bool res = false;
        backtrace(dict, s, res, 0);
        return res;
    }

    void backtrace(unordered_map<char, vector<string>> &dict, string &s, bool &res, int start) {
        if (res == true) {
            return;
        }

        if (start == s.length()) {
            res = true;
            return;
        }

        if (dict.find(s[start]) == dict.end()) {
            return;
        }

        for (int i = 0; i < dict[s[start]].size(); i++) {
            string words = dict[s[start]][i];
            if (s.substr(start, words.size()) == words) {
                backtrace(dict, s, res, start+words.size());
            };
        }
    }

    bool wordBreakNew(string s, vector<string>& wordDict) {
        vector<bool> dp(s.size()+1, false);
        unordered_set<string> candidates(wordDict.begin(), wordDict.end());
        dp[0] = true;

        for (int i = 1; i < s.size() + 1; i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] == true && candidates.find(s.substr(j, i - j)) != candidates.end()) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[s.size()];
    }
};

int main() {
    Solution s;
    vector<string> array = {"cog","news"};
    cout << s.wordBreakNew("co", array);
}
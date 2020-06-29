#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;
// Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

// For example, given n = 3, a solution set is:

// [
//   "((()))",
//   "(()())",
//   "(())()",
//   "()(())",
//   "()()()"
// ]


class Solution {
public:
    map<int, vector<string>> store_map;

    vector<string> generateParenthesis(int n) {
        vector<string> res;
        if (n <= 0) {
            return res;
        }
        if (n == 1) {
            res.push_back("()");
            return res;
        }

        if (store_map.find(n) != store_map.end()) {
            return store_map[n];
        }
        
        set<string> words;
        for (int i = 1; i < n; i++) {
            auto left = generateParenthesis(i);
            auto right = generateParenthesis(n - i);

            for (int k = 0; k < left.size(); k++) {
                for (int j = 0; j < right.size(); j++) {
                    string word = string(left[k] + right[j]);
                    words.insert(word);
                }
            }
        }

        // only one part
        auto previous = generateParenthesis(n - 1);
        for (int j = 0; j < previous.size(); j++) {
            string word = string('('+ previous[j] + ')');
            words.insert(word);
        }
        auto iter = words.begin();
        vector<string> answer;
        while (iter != words.end()) {
            answer.push_back(*iter);
            iter++;
        }
        store_map[n] = answer;
        return answer;
    }

    vector<string> generateParenthesisNew(int n) {
        vector<vector<string>> dp;
        vector<string> item = {""};
        dp.push_back(item);

        for (int i = 1; i < n+1; i++) {
            vector<string> new_item = {};
            for (int chose = 0; chose < i; chose++) {
                for (int k = 0; k < dp[chose].size(); k++) {
                    for (int j = 0; j < dp[i-chose-1].size(); j++) {
                        string word = string('(' + dp[chose][k] + ')' + dp[i-chose-1][j]);
                        new_item.push_back(word);
                    }
                }
            }
            dp.push_back(new_item); 
        }
        return dp[n];
    }
};


int main() {
    Solution s;
    auto res = s.generateParenthesisNew(4);

    for (auto e: res) {
        cout << e << endl;
    }
    cout << endl;
}






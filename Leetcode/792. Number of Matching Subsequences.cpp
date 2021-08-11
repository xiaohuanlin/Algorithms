#include <vector>
#include <stack>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

// A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

// For example, "ace" is a subsequence of "abcde".
 

// Example 1:

// Input: s = "abcde", words = ["a","bb","acd","ace"]
// Output: 3
// Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
// Example 2:

// Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
// Output: 2
 

// Constraints:

// 1 <= s.length <= 5 * 10^4
// 1 <= words.length <= 5000
// 1 <= words[i].length <= 50
// s and words[i] consist of only lowercase English letters.


class Solution {
public:
    struct Node {
        int index_;
        vector<Node*> children_;
        Node(int index = -1): index_(index), children_(26, nullptr) {};
    };
    

    int numMatchingSubseq(string s, vector<string>& words) {
        vector<vector<int>> s_indexs(26, vector<int>());
        for (int i = 0; i < s.size(); ++i) {
            s_indexs[s[i] - 'a'].push_back(i);
        }

        Node dummy, error, end;
        int result = 0;
        for (auto& word : words) {
            Node* iter = &dummy;
            for (int i = 0; i < word.size(); ++i) {
                if (iter == &error) {
                    // find not valid result
                    break;
                }
                auto next = iter->children_[word[i] - 'a'];
                if (next == &error) {
                    break;
                } else if (next == nullptr) {
                    // find its first position after iter index
                    auto& check_vector = s_indexs[word[i] - 'a'];
                    auto iterator = upper_bound(check_vector.begin(), check_vector.end(), iter->index_);
                    Node* node;
                    if (iterator == check_vector.end()) {
                        // not suitable for our result
                        node = &error;
                    } else {
                        node = new Node(*iterator);
                        if (i == word.size() - 1) {
                            result++;
                        }
                    }
                    iter->children_[word[i] - 'a'] = node;
                    iter = node;
                } else {
                    // find if there have recorded the index of c
                    iter = next;
                    if (i == word.size() - 1) {
                        result++;
                    }
                }
            }
        }
        return result;
    }
};

int main() {
    Solution s;
    vector<tuple<tuple<string, vector<string>>, int>> test_cases {
        {{"vvvvm", {"vm","vm","vn","vn"}}, 2},
        {{"dsahjpjauf", {"ahjpjau","ja","ahbwzgqnuk","tnmlanowax"}}, 2},
        {{"abcde", {"a","bb","acd","ace"}}, 3},
        {{"rwpddkvbnnuglnagtvamxkqtwhqgwbqgfbvgkwyuqkdwhzudsxvjubjgloeofnpjqlkdsqvruvabjrikfwronbrdyyjnakstqjac", {"wpddkvbnn","lnagtva","kvbnnuglnagtvamxkqtwhqgwbqgfbvgkwyuqkdwhzudsxvju","rwpddkvbnnugln","gloeofnpjqlkdsqvruvabjrikfwronbrdyyj","vbgeinupkvgmgxeaaiuiyojmoqkahwvbpwugdainxciedbdkos","mspuhbykmmumtveoighlcgpcapzczomshiblnvhjzqjlfkpina","rgmliajkiknongrofpugfgajedxicdhxinzjakwnifvxwlokip","fhepktaipapyrbylskxddypwmuuxyoivcewzrdwwlrlhqwzikq","qatithxifaaiwyszlkgoljzkkweqkjjzvymedvclfxwcezqebx"}}, 5},
    };

    for (auto& test_case: test_cases) {
        assert(s.numMatchingSubseq(get<0>(get<0>(test_case)),get<1>(get<0>(test_case))) == get<1>(test_case));
    }
}
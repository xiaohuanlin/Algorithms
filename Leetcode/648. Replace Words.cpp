#include <vector>
#include <iostream>
#include <tuple>
#include <unordered_set>
#include <assert.h>
using namespace std;

// In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. For example, when the root "an" is followed by the successor word "other", we can form a new word "another".

// Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

// Return the sentence after the replacement.

 

// Example 1:

// Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
// Output: "the cat was rat by the bat"
// Example 2:

// Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
// Output: "a a b c"
// Example 3:

// Input: dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
// Output: "a a a a a a a a bbb baba a"
// Example 4:

// Input: dictionary = ["catt","cat","bat","rat"], sentence = "the cattle was rattled by the battery"
// Output: "the cat was rat by the bat"
// Example 5:

// Input: dictionary = ["ac","ab"], sentence = "it is abnormal that this solution is accepted"
// Output: "it is ab that this solution is ac"
 

// Constraints:

// 1 <= dictionary.length <= 1000
// 1 <= dictionary[i].length <= 100
// dictionary[i] consists of only lower-case letters.
// 1 <= sentence.length <= 10^6
// sentence consists of only lower-case letters and spaces.
// The number of words in sentence is in the range [1, 1000]
// The length of each word in sentence is in the range [1, 1000]
// Each two consecutive words in sentence will be separated by exactly one space.
// sentence does not have leading or trailing spaces.


class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        unordered_set<string> sets;
        for (auto& str : dictionary) {
            sets.insert(str);
        }

        string res;
        string word;
        unordered_set<string>::iterator prefix;

        for (int i = 0; i < sentence.length(); i++) {
            if (sentence[i] == ' ') {
                res += word;
                word.clear();
                if (i != sentence.length()) {
                    // we should not push last space symbol
                    res.push_back(' ');
                }
                continue;
            }

            word.push_back(sentence[i]);
            if ((prefix = sets.find(word)) != sets.end()) {
                res += *prefix;
                word.clear();
                while (i < sentence.length() && sentence[i] != ' ') {
                    i++;
                }
                if (i != sentence.length()) {
                    // we should not push last space symbol
                    res.push_back(' ');
                }
            }
        }
        
        if (!word.empty()) {
            res += word;
        }

        return res;
    }
};

int main() {
    Solution s;
    vector<tuple<vector<string>, string, string>> test_cases {
        {{"a", "b"}, "the ab cde", "the a cde"},
        {{"cat","bat","rat"}, "the cattle was rattled by the battery", "the cat was rat by the bat"},
        {{"a","b","c"}, "aadsfasf absbs bbab cadsfafs", "a a b c"},
        {{"a", "aa", "aaa", "aaaa"}, "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa", "a a a a a a a a bbb baba a"},
        {{"catt","cat","bat","rat"}, "the cattle was rattled by the battery", "the cat was rat by the bat"},
        {{"ac","ab"}, "it is abnormal that this solution is accepted", "it is ab that this solution is ac"}
    };

    for (auto& test_case: test_cases) {
        assert(s.replaceWords(get<0>(test_case), get<1>(test_case)) == get<2>(test_case));
    }
}
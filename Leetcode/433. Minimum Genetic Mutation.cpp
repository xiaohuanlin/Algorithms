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


// A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

// Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

// For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

// Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

// Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

// Note:

// Starting point is assumed to be valid, so it might not be included in the bank.
// If multiple mutations are needed, all mutations during in the sequence must be valid.
// You may assume start and end string is not the same.
 

// Example 1:

// start: "AACCGGTT"
// end:   "AACCGGTA"
// bank: ["AACCGGTA"]

// return: 1
 

// Example 2:

// start: "AACCGGTT"
// end:   "AAACGGTA"
// bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

// return: 2
 

// Example 3:

// start: "AAAAACCC"
// end:   "AACCCCCC"
// bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

// return: 3


class Solution {
public:
    int minMutation(string start, string end, vector<string>& bank) {
        int min_value = core(start, end, bank);
        return min_value == INT32_MAX? -1: min_value;
    }
    
    int core(string start, string end, vector<string>& bank) {
        if (start == end) {
            return 0;
        }
        int min_value = INT32_MAX;
        for (int j = 0; j < bank.size(); ++j) {
            string current = bank[j];
            int count = 0;
            for (int i = 0; i < start.size(); ++i) {
                if (start[i] != current[i]) {
                    count++;
                }
            }
            if (count == 1) {
                bank.erase(bank.begin() + j);
                int tmp = core(current, end, bank);
                tmp = tmp == INT32_MAX ? INT32_MAX: tmp + 1;
                min_value = min(min_value, tmp);
                bank.insert(bank.begin() + j, current);
            }
        }
        return min_value;
    }
};

int main() {
    Solution s;
    vector<string> array {"AACCGGTA", "AACCGCTA", "AAACGGTA"};
    cout << s.minMutation("AACCGGTT", "AAACGGTA", array);
}
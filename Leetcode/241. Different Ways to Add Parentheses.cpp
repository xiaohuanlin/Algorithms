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


// Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

// Example 1:

// Input: "2-1-1"
// Output: [0, 2]
// Explanation: 
// ((2-1)-1) = 0 
// (2-(1-1)) = 2
// Example 2:

// Input: "2*3-4*5"
// Output: [-34, -14, -10, -10, 10]
// Explanation: 
// (2*(3-(4*5))) = -34 
// ((2*3)-(4*5)) = -14 
// ((2*(3-4))*5) = -10 
// (2*((3-4)*5)) = -10 
// (((2*3)-4)*5) = 10


class Solution {
public:
    vector<int> diffWaysToCompute(string input) {
        vector<int> elements;
        vector<char> opers;
        int count = 0;
        while (count < input.length()) {
            if (isdigit(input[count])) {
                int start = count;
                while (count < input.length() && isdigit(input[count])) {
                    count++;
                }
                elements.push_back(stoi(input.substr(start, count - start)));
            } 
            if (count < input.length()) {
                opers.push_back(input[count]);
            }
            count++;
        }
        vector<vector<vector<int>>> dps(elements.size(), vector<vector<int>>(elements.size(), vector<int>()));
        for (int end = 0; end < elements.size(); end++) {
            for (int start = end; start >= 0; start--) {
                if (start == end) {
                    dps[start][end].push_back(elements[start]);
                } else if (start == end - 1) {
                    int value;
                    switch (opers[start]) {
                        case '+': {
                            value = elements[start] + elements[end];
                            break;
                        }
                        case '-': {
                            value = elements[start] - elements[end];
                            break;
                        }
                        case '*': {
                            value = elements[start] * elements[end];
                            break;
                        }
                    }
                    dps[start][end].push_back(value);
                } else {
                    for (int i = start; i < end; i++) {
                        for (auto m: dps[start][i]) {
                            for (auto l: dps[i+1][end]) {
                                int value;
                                switch (opers[i]) {
                                    case '+': {
                                        value = m + l;
                                        break;
                                    }
                                    case '-': {
                                        value = m - l;
                                        break;
                                    }
                                    case '*': {
                                        value = m * l;
                                        break;
                                    }
                                }
                                dps[start][end].push_back(value);
                            }
                        }
                    }
                }

            }
        }
        return dps[0][elements.size()-1];
    }
};

int main() {
    Solution s;
    auto res = s.diffWaysToCompute("2+5*3");
    for (auto e: res) {
        cout << e << ',';
    }
    cout << endl;
}
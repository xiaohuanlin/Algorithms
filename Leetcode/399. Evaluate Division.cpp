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
#include <numeric>
using namespace std;


// Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

// Example:
// Given a / b = 2.0, b / c = 3.0.
// queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
// return [6.0, 0.5, -1.0, 1.0, -1.0 ].

// The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

// According to the example above:

// equations = [ ["a", "b"], ["b", "c"] ],
// values = [2.0, 3.0],
// queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 

// The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
 
class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        unordered_map<string, vector<pair<string, double>>> adjacents;
        for (int i = 0; i < equations.size(); i++) {
            auto &item = equations[i];
            double value = values[i];
            if (item[0] > item[1]) {
            }
        }
    }
};

int main() {
    Solution s;
    vector<vector<string>> array = {{"a", "b"}, {"b", "c"}};
    vector<double> value = {2.0, 3.0};
    vector<vector<string>> query = {
        {"a", "c"}, {"b", "a"}, {"a", "e"}, {"a", "a"}, {"x", "x"}
    };
    auto res = s.calcEquation(array, value, query);

    for (auto e: res) {
        cout << e << endl;
    }
    cout << endl;
}
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
    struct ratio {
        double num;
        double den;
        ratio(double _num, double _den): num(_num), den(_den) {};
        ratio operator*(ratio &a) {
            return move(ratio(num * a.num, den * a.den));
        }
    };

public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        unordered_map<string, vector<pair<string, ratio>>> adjacents;
        for (int i = 0; i < equations.size(); i++) {
            auto &item = equations[i];
            double value = values[i];

            if (adjacents.find(item[1]) == adjacents.end()) {
                adjacents[item[1]] = vector<pair<string, ratio>>();
            }
            adjacents[item[1]].push_back(make_pair(item[0], ratio(1, value)));

            if (adjacents.find(item[0]) == adjacents.end()) {
                adjacents[item[0]] = vector<pair<string, ratio>>();
            }
            adjacents[item[0]].push_back(make_pair(item[1], ratio(value, 1)));
        }

        vector<ratio> path;
        vector<double> res;
        unordered_set<string> choices;
        for (int j = 0; j < queries.size(); j++) {
            double answer;
            if (queries[j][0] > queries[j][1]) {
                if (adjacents.find(queries[j][1]) == adjacents.end()) {
                    res.push_back(-1);
                } else if (find_res(answer, adjacents, path, choices, queries[j][1], queries[j][0])) {
                    res.push_back(1 / answer);
                } else {
                    res.push_back(-1);
                };
            } else {
                if (adjacents.find(queries[j][0]) == adjacents.end()) {
                    res.push_back(-1);
                } else if (find_res(answer, adjacents, path, choices, queries[j][0], queries[j][1])) {
                    res.push_back(answer);
                } else {
                    res.push_back(-1);
                }
            }
            path.clear();
            choices.clear();
        }
        return move(res);
    }
    
    bool find_res(double &res, unordered_map<string, vector<pair<string, ratio>>> &adjacents,
            vector<ratio> &path, unordered_set<string> &choices, string &start, string &end)
    {
        if (start == end) {
            // get the result
            ratio t(1, 1);
            for (int i = 0; i < path.size(); i++) {
                t = t * path[i];
            }
            res = t.num / t.den;
            return true;    
        }

        res = -1;
        if (adjacents.find(start) == adjacents.end()) {
            return false;
        }
        auto &all_things = adjacents[start];
        for (int i = 0; i < all_things.size(); i++) {
            if (choices.find(all_things[i].first) != choices.end()) {
                continue;
            }
            path.push_back(all_things[i].second);
            choices.insert(all_things[i].first);
            if (find_res(res, adjacents, path, choices, all_things[i].first, end)) {
                return true;
            }
            choices.erase(all_things[i].first);
            path.pop_back();
        }
        return false;
    }
};

int main() {
    Solution s;
    vector<vector<string>> array = {{"a", "b"}, {"b", "c"}};
    vector<double> value = {2.0, 3.0};
    vector<vector<string>> query = {
        {"x", "x"}
    };
    auto res = s.calcEquation(array, value, query);

    for (auto e: res) {
        cout << e << endl;
    }
    cout << endl;
}
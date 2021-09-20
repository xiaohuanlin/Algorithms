#include <vector>
#include <queue>
#include <unordered_map>
#include <iostream>
#include <tuple>
#include <assert.h>
#include <algorithm>
using namespace std;


// You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

// Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

// If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

 

// Example 1:



// Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
// Output: 0.25000
// Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
// Example 2:



// Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
// Output: 0.30000
// Example 3:



// Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
// Output: 0.00000
// Explanation: There is no path between 0 and 2.
 

// Constraints:

// 2 <= n <= 10^4
// 0 <= start, end < n
// start != end
// 0 <= a, b < n
// a != b
// 0 <= succProb.length == edges.length <= 2*10^4
// 0 <= succProb[i] <= 1
// There is at most one edge between every two nodes.


class Solution {
    struct Node {
        int id_;
        double probability_;
        Node(int id, double probability): id_(id), probability_(probability) {};
    };
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start, int end) {
        unordered_map<int, vector<tuple<int, double>>> maps;
        for (int i = 0; i < edges.size(); i++) {
            maps[edges[i][0]].push_back({edges[i][1], succProb[i]});
            maps[edges[i][1]].push_back({edges[i][0], succProb[i]});
        }

        vector<double> probabilities(n, 0);
        probabilities[start] = 1;

        auto func = [] (const Node& a, const Node& b) {
            return a.probability_ < b.probability_;
        };

        priority_queue<Node, vector<Node>, decltype(func)> candidates(func);
        candidates.push({start, 1});
        while (!candidates.empty()) {
            auto node = candidates.top();
            candidates.pop();

            if (node.id_ == end) {
                return node.probability_;
            }

            if (node.probability_ < probabilities[node.id_]) {
                continue;
            }

            for (auto& pair: maps[node.id_]) {
                int next_id = get<0>(pair);
                double next_step_prob = get<1>(pair);

                double next_total_prob = node.probability_ * next_step_prob;
                if (next_total_prob > probabilities[next_id]) {
                    probabilities[next_id] = next_total_prob;
                    candidates.push({next_id, next_total_prob});
                }
            }
        }
        return 0;
    }
};

int main() {
    Solution s;
    vector<
        tuple<
            tuple<
                int, vector<vector<int>>, vector<double>, int, int
            >, 
            double
        >
    > test_cases {
        {
            {3, {{0, 1}, {1, 2}, {0, 2}}, {0.5, 0.5, 0.2}, 0, 2},
            0.25
        },
        {
            {3, {{0, 1}, {1, 2}, {0, 2}}, {0.5, 0.5, 0.3}, 0, 2},
            0.3
        },
        {
            {3, {{0, 1}}, {0.5}, 0, 2},
            0
        },
    };

    for (auto& test_case: test_cases) {
        assert(s.maxProbability(
                    get<0>(get<0>(test_case)),
                    get<1>(get<0>(test_case)),
                    get<2>(get<0>(test_case)),
                    get<3>(get<0>(test_case)),
                    get<4>(get<0>(test_case))
                ) == get<1>(test_case)
        );
    }
}
#include <vector>
#include <queue>
#include <unordered_map>
#include <iostream>
#include <tuple>
#include <assert.h>
#include <algorithm>
using namespace std;


// You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

// We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

// Example 1:


// Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
// Output: 2
// Example 2:

// Input: times = [[1,2,1]], n = 2, k = 1
// Output: 1
// Example 3:

// Input: times = [[1,2,1]], n = 2, k = 2
// Output: -1
 

// Constraints:

// 1 <= k <= n <= 100
// 1 <= times.length <= 6000
// times[i].length == 3
// 1 <= ui, vi <= n
// ui != vi
// 0 <= wi <= 100
// All the pairs (ui, vi) are unique. (i.e., no multiple edges.)


class Solution {
    struct Node {
        int val_;
        int distance_;
        Node(int val, int distance): val_(val), distance_(distance) {};
    };

public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        // transfer to edges
        unordered_map<int, vector<vector<int>>> edges;
        for (auto& time: times) {
            edges[time[0]].push_back({time[1], time[2]});
        }

        // record min distance
        vector<int> distance(n + 1, INT32_MAX);
        distance[k] = 0;

        auto func = [] (const Node& a, const Node& b) {
            return a.distance_ < b.distance_;
        };

        priority_queue<Node, vector<Node>, decltype(func)> candidates(func);
        candidates.push({k, 0});

        while (!candidates.empty()) {
            auto node = candidates.top();
            candidates.pop();

            if (node.distance_ > distance[node.val_]) {
                continue;
            }

            for (auto& item: edges[node.val_]) {
                int& next_node = item[0];
                int& next_distance = item[1];
                int distance_to_next = node.distance_ + next_distance;
                if (distance_to_next < distance[next_node]) {
                    distance[next_node] = distance_to_next;
                    candidates.push({next_node, distance[next_node]});
                }
            }
        }

        int max_v = 0;
        for (int i = 1; i < distance.size(); i++) {
            if (distance[i] == INT32_MAX) {
                return -1;
            }
            max_v = max(max_v, distance[i]);
        }
        return max_v;
    }
};

int main() {
    Solution s;
    vector<tuple<tuple<vector<vector<int>>, int, int>, int>> test_cases {
        {{{{2,1,1},{2,3,1},{3,4,1}}, 4, 2}, 2},
        {{{{1,2,1}}, 2, 1}, 1},
        {{{{1,2,1}}, 2, 2}, -1},
    };

    for (auto& test_case: test_cases) {
        assert(s.networkDelayTime(get<0>(get<0>(test_case)), get<1>(get<0>(test_case)), get<2>(get<0>(test_case))) == get<1>(test_case));
    }
}
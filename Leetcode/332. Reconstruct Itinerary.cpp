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

// Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

// Note:

// If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
// All airports are represented by three capital letters (IATA code).
// You may assume all tickets form at least one valid itinerary.
// One must use all the tickets once and only once.
// Example 1:

// Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
// Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
// Example 2:

// Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
// Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
// Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
//              But it is larger in lexical order.


class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
		vector<string> res = {"JFK"};
		unordered_map<string, vector<string>> adj;
		for (int i = 0; i < tickets.size(); i++) {
			if (adj.find(tickets[i][0]) == adj.end()) {
				adj[tickets[i][0]] = vector<string>();
			}
			adj[tickets[i][0]].push_back(tickets[i][1]);
		}
		for (auto iter = adj.begin(); iter != adj.end(); iter++) {
			sort(iter->second.begin(), iter->second.end());
		}

		backtrace(res, adj);
		return res;
    }

	bool backtrace(vector<string> &res, unordered_map<string, vector<string>> &adj) {
		int count = 0;
		for (auto iter = adj.begin(); iter != adj.end(); iter++) {
			if (iter->second.empty()){
				count ++;
			} else {
				break;
			}
		}
		if (count == adj.size()) {
			return true;
		}

		string pick_string = res.back();
		vector<string> &ad_vector = adj[pick_string];
		for (int i = 0; i < ad_vector.size(); i ++) {
			vector<string> edge = {pick_string, ad_vector[i]};
			res.push_back(ad_vector[i]);
			ad_vector.erase(ad_vector.begin() + i);
			if (backtrace(res, adj)) {
				return true;
			}
			ad_vector.insert(ad_vector.begin() + i, edge[1]);
			res.pop_back();
		}
		return false;
	}
};

int main() {
	Solution s;

	vector<vector<string>> array = {
		{"EZE","AXA"},{"TIA","ANU"},{"ANU","JFK"},{"JFK","ANU"},{"ANU","EZE"},{"TIA","ANU"},{"AXA","TIA"},{"TIA","JFK"},{"ANU","TIA"},{"JFK","TIA"}
	};
	auto res = s.findItinerary(array);
	for (auto e: res) {
		cout << e << ',';
	}
	cout << endl;
}
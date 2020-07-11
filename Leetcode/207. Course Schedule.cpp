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


// There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

// Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

// Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

// Example 1:

// Input: numCourses = 2, prerequisites = [[1,0]]
// Output: true
// Explanation: There are a total of 2 courses to take. 
//              To take course 1 you should have finished course 0. So it is possible.
// Example 2:

// Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
// Output: false
// Explanation: There are a total of 2 courses to take. 
//              To take course 1 you should have finished course 0, and to take course 0 you should
//              also have finished course 1. So it is impossible.
 

// Constraints:

// The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
// You may assume that there are no duplicate edges in the input prerequisites.
// 1 <= numCourses <= 10^5


class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, vector<int>> nextcourses;
        unordered_set<int> visited;

        for (int i = 0; i < prerequisites.size(); i++) {
            if (prerequisites[i].empty()) {
                continue;
            }
            if (nextcourses.find(prerequisites[i][1]) == nextcourses.end()) {
                nextcourses[prerequisites[i][1]] = vector<int>();
            }
            nextcourses[prerequisites[i][1]].push_back(prerequisites[i][0]);
        }

        stack<int> candidates;
        for (auto iter = nextcourses.begin(); iter != nextcourses.end(); iter++) {
            candidates.push((*iter).first);
            while (!candidates.empty()) {
                auto item = candidates.top();
                candidates.pop();

                if (visited.find(item) != visited.end()) {
                    return false;
                }
                if (nextcourses.find(item) == nextcourses.end()) {
                    continue;
                }
                visited.insert(item);

                for (int i = 0; i < nextcourses[item].size(); i++) {
                    candidates.push(nextcourses[item][i]);
                }
            }
            visited.clear();
        }

        return true;
    }
};

int main() {
    Solution s;
    vector<vector<int>> array = {
        {0,1},
        {0,2},
        {1,2},
    };
    cout << s.canFinish(5, array);
    // todo
}
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
        unordered_map<int, vector<int>> adjacent;
        unordered_map<int, int> store;
        for (int i = 0; i < prerequisites.size(); i++) {
            if (adjacent.find(prerequisites[i][1]) == adjacent.end()) {
                adjacent[prerequisites[i][1]] = vector<int>();
            }
            adjacent[prerequisites[i][1]].push_back(prerequisites[i][0]);

            if (store.find(prerequisites[i][0]) == store.end()) {
                store[prerequisites[i][0]] = 0;
            }
            store[prerequisites[i][0]]++;
        }

        bool end = true;
        while (end) {
            end = false;
            for (auto iter = adjacent.begin(); iter != adjacent.end(); iter++) {
                if (store.find((*iter).first) == store.end()) {
                    auto item = (*iter).second;
                    for (int i = 0; i < item.size(); i++) {
                        if (--store[item[i]] == 0) {
                            store.erase(item[i]);
                        }
                    }
                    adjacent.erase((*iter).first);
                    end = true;
                    break;
                }
            }
        }

        return adjacent.empty();
    }

    bool canFinishNew(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, vector<int>> adjacent;
        for (int i = 0; i < prerequisites.size(); i++) {
            if (adjacent.find(prerequisites[i][1]) == adjacent.end()) {
                adjacent[prerequisites[i][1]] = vector<int>();
            }
            adjacent[prerequisites[i][1]].push_back(prerequisites[i][0]);
        }
        unordered_set<int> path, done;
        
        bool result = true;
        for (auto iter = adjacent.begin(); iter != adjacent.end(); iter++) {
            if (done.find((*iter).first) != done.end()) {
                continue;
            }

            done.insert((*iter).first);
            dfs(adjacent, path, done, (*iter).first, result);
            if (!result) {
                return false;
            }
        }
        return true;
    }

    void dfs(unordered_map<int, vector<int>> &adjacent, unordered_set<int> &path, unordered_set<int> &done, 
            int start, bool &result) {
        if (!result || path.find(start) != path.end()) {
            result = false;
            return;
        }

        if (adjacent.find(start) == adjacent.end()) {
            return;
        }

        done.insert(start);
        path.insert(start);

        for (int i = 0; i < adjacent[start].size(); i++) {
            dfs(adjacent, path, done, adjacent[start][i], result);

            if (!result) {
                return;
            }
        }

        path.erase(start);
    }
};

int main() {
    Solution s;
    vector<vector<int>> array = {
        {1,0},
    };
    cout << s.canFinishNew(5, array);
}
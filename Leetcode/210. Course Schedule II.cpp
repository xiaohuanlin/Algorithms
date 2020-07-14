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


// There are a total of n courses you have to take, labeled from 0 to n-1.

// Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

// Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

// There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

// Example 1:

// Input: 2, [[1,0]] 
// Output: [0,1]
// Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
//              course 0. So the correct course order is [0,1] .
// Example 2:

// Input: 4, [[1,0],[2,0],[3,1],[3,2]]
// Output: [0,1,2,3] or [0,2,1,3]
// Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
//              courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
//              So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
// Note:

// The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
// You may assume that there are no duplicate edges in the input prerequisites.


class Solution {
public:

    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adjacent(numCourses, vector<int>());
        for (int i = 0; i < prerequisites.size(); i++) {
            adjacent[prerequisites[i][1]].push_back(prerequisites[i][0]);
        }

        vector<int> path(numCourses, false), done(numCourses, false);
        vector<int> res;
        bool valid = true;
        for (int i = 0; i < numCourses; i++) {
            if (done[i]) {
                continue;
            }

            dfs(res, adjacent, path, done, i, valid);
        }
        if (!valid) {
            res.clear();
        }
        reverse(res.begin(), res.end());
        return res;
    }

    void dfs(vector<int> &res, vector<vector<int>> &adjacent, vector<int> &path, vector<int> &done, int start, bool &valid) {
        if (path[start] || !valid) {
            valid = false;
            return;
        }

        if (done[start]) {
            return;
        }

        done[start] = true;
        path[start] = true;
        for (int i = 0; i < adjacent[start].size(); i++) {
            dfs(res, adjacent, path, done, adjacent[start][i], valid);
        }
        path[start] = false;
        
        if (valid) {
            res.push_back(start);
        }
    }
};

int main() {
    Solution s;
    vector<vector<int>> array = {
        {1,0},
    };
    auto res = s.findOrder(5, array);
    for (auto e: res) {
        cout << e << ',';
    }
    cout << endl;
}
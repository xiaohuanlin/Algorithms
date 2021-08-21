#include <vector>
#include <unordered_map>
#include <set>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;


// You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

// Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.

 

// Example 1:


// Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
// Output: 4
// Example 2:


// Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
// Output: 2
 

// Constraints:

// 1 <= points.length <= 500
// points[i].length == 2
// 0 <= xi, yi <= 4 * 10^4
// All the given points are unique.



class Solution {
public:
    int minAreaRect(vector<vector<int>>& points) {
        unordered_map<int, set<int>> maps;
        for (auto& point: points) {
            maps[point[0]].insert(point[1]);
        }

        int ans = INT32_MAX;
        for (auto i = maps.begin(); i != maps.end(); i++) {
            for (auto j = next(i); j != maps.end(); j++) {
                // fix two x coords
                if (i->second.size() < 2 || j->second.size() < 2) {
                    continue;
                }
                vector<int> intersection;
                set_intersection(
                    i->second.begin(), i->second.end(),
                    j->second.begin(), j->second.end(),
                    back_inserter(intersection)
                );

                if (intersection.size() < 2) {
                    continue;
                }

                for (int k = 0; k < intersection.size() - 1; k++) {
                    ans = min(abs(i->first - j->first) * (intersection[k + 1] - intersection[k]), ans);
                }
            }
        }

        return ans == INT32_MAX ? 0 : ans;
    }
};

int main() {
    Solution s;
    vector<tuple<vector<vector<int>>, int>> test_cases {
        {{{1,1},{1,3},{3,1},{3,3},{2,2}}, 4},
        {{{1,1},{1,3},{3,1},{3,3},{4,1},{4,3}}, 2},
    };

    for (auto& test_case: test_cases) {
        assert(s.minAreaRect(get<0>(test_case)) == get<1>(test_case));
    }
}
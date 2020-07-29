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
#include <queue>
using namespace std;

// Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

// Note that it is the kth smallest element in the sorted order, not the kth distinct element.

// Example:

// matrix = [
//    [ 1,  5,  9],
//    [10, 11, 13],
//    [12, 13, 15]
// ],
// k = 8,

// return 13.
// Note: 
// You may assume k is always valid, 1 ≤ k ≤ n2.


class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        if (matrix.empty() || matrix[0].empty()) {
            return -1;
        }

        auto func = [&] (pair<int, int> &a, pair<int, int> &b) {
            return matrix[a.first][a.second] > matrix[b.first][b.second];
        };

        priority_queue<pair<int, int>, vector<pair<int,int>>, decltype(func)> queue(func);
        for (int i = 0; i < matrix[0].size(); i++) {
            queue.emplace(make_pair(i, 0));
        }

        int count = 0;
        while (count < k - 1) {
            auto item = queue.top();
            queue.pop();
            if (item.second + 1 < matrix[0].size()) {
                queue.emplace(make_pair(item.first, item.second + 1));
            }
            count ++;
        }
        return matrix[queue.top().first][queue.top().second];
    }
};

int main() {
    Solution s;
    vector<vector<int>> array {
        {1,5,9},
        {10,11,13},
        {12,13,15},
    };
    cout << s.kthSmallest(array, 9);
}

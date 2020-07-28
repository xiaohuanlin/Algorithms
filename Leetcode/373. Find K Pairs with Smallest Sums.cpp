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

// You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

// Define a pair (u,v) which consists of one element from the first array and one element from the second array.

// Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

// Example 1:

// Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
// Output: [[1,2],[1,4],[1,6]] 
// Explanation: The first 3 pairs are returned from the sequence: 
//              [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
// Example 2:

// Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
// Output: [1,1],[1,1]
// Explanation: The first 2 pairs are returned from the sequence: 
//              [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
// Example 3:

// Input: nums1 = [1,2], nums2 = [3], k = 3
// Output: [1,3],[2,3]
// Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]


class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        // some thing like generate tree
        vector<vector<int>> res;
        if (nums1.empty() || nums2.empty() || k <= 0) {
            return res;
        }
        auto func = [&](pair<int, int> &a, pair<int, int> &b) {
            return (nums1[a.first] + nums2[a.second]) > (nums1[b.first] + nums2[b.second]);
        };
        priority_queue<pair<int, int>, vector<pair<int,int>>, decltype(func)> que(func); 

        // put nums1 first
        for (int i = 0; i < min(int(nums1.size()), k); i++) {
            que.emplace(i, 0);
        }

        int count = 0;
        while (!que.empty() && count < k) {
            auto item = que.top();
            vector<int> tem = {nums1[item.first], nums2[item.second]};
            res.push_back(move(tem));
            que.pop();

            if (item.second + 1 < nums2.size()) {
                que.emplace(item.first, item.second+1);
            }
            count ++;
        }
        return res;
    }
};

int main() {
    Solution s;
    vector<int> array1 = {1,7,11}, array2 = {2,4,6};
    auto res = s.kSmallestPairs(array1, array2, 3);
    for (auto e: res) {
        for (auto l: e) {
            cout << l << ',';
        }
        cout << endl;
    }
}

#include <vector>
#include <set>
#include <iostream>
#include <tuple>
#include <assert.h>
#include <algorithm>
using namespace std;

// You are given two integer arrays nums1 and nums2 both of the same length. The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].

// Return any permutation of nums1 that maximizes its advantage with respect to nums2.

 

// Example 1:

// Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
// Output: [2,11,7,15]
// Example 2:

// Input: nums1 = [12,24,8,32], nums2 = [13,25,32,11]
// Output: [24,32,8,12]
 

// Constraints:

// 1 <= nums1.length <= 10^5
// nums2.length == nums1.length
// 0 <= nums1[i], nums2[i] <= 10^9

class Solution {
public:
    vector<int> advantageCount(vector<int>& nums1, vector<int>& nums2) {
        // binary search can use the multiset structure to realize this process
        multiset<int> candidate(nums1.begin(), nums1.end());

        vector<int> res;
        for (auto& num : nums2) {
            auto iter = candidate.upper_bound(num);
            if (iter == candidate.end()) {
                iter = candidate.begin();
            }
            res.push_back(*iter);
            candidate.erase(iter);
        }

        return res;
    }
};

int main() {
    Solution s;
    vector<tuple<tuple<vector<int>, vector<int>>, vector<int>>> test_cases {
        {{{}, {}}, {}},
        {{{1,2,3}, {4,5,6}}, {1,2,3}},
        {{{6,5,4}, {1,2,3}}, {4,5,6}},
        {{{2,7,11,15}, {1,10,4,11}}, {2,11,7,15}},
        {{{12,24,8,32}, {13,25,32,11}}, {24,32,8,12}},
    };

    for (auto& test_case: test_cases) {
        assert(s.advantageCount(get<0>(get<0>(test_case)), get<1>(get<0>(test_case))) == get<1>(test_case));
    }
}
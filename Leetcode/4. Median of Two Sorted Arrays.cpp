#include <vector>
#include <iostream>
using namespace std;
// There are two sorted arrays nums1 and nums2 of size m and n respectively.

// Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

// You may assume nums1 and nums2 cannot be both empty.

// Example 1:

// nums1 = [1, 3]
// nums2 = [2]

// The median is 2.0
// Example 2:

// nums1 = [1, 2]
// nums2 = [3, 4]

// The median is (2 + 3)/2 = 2.5

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;

        auto iter1 = nums1.begin();
        auto iter2 = nums2.begin();

        while (iter1 != nums1.end() && iter2 != nums2.end()) {
            if (*iter1 > *iter2) {
                res.push_back(*iter2++);
            } else {
                res.push_back(*iter1++);
            }
        }

        while (iter1 != nums1.end()) {
            res.push_back(*iter1++);
        }

        while (iter2 != nums2.end()) {
            res.push_back(*iter2++);
        }

        int middle = res.size() / 2;
        if ((res.size() % 2) == 0) {
            return (res[middle] + res[middle - 1]) / 2.0;
        } else {
            return res[middle];
        }
    }
};


int main() {
    Solution s;
    vector<int> array1 = {7, 8, 9};
    vector<int> array2 = {1, 2, 6};
    cout << s.findMedianSortedArrays(array1, array2);
}
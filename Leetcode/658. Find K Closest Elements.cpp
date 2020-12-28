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


// Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

// An integer a is closer to x than an integer b if:

// |a - x| < |b - x|, or
// |a - x| == |b - x| and a < b
 

// Example 1:

// Input: arr = [1,2,3,4,5], k = 4, x = 3
// Output: [1,2,3,4]
// Example 2:

// Input: arr = [1,2,3,4,5], k = 4, x = -1
// Output: [1,2,3,4]
 

// Constraints:

// 1 <= k <= arr.length
// 1 <= arr.length <= 104
// Absolute value of elements in the array and x will not exceed 104


class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        if (k >= arr.size()) {
            return arr;
        }

        int start = 0;
        int end = arr.size();
        while (start < end) {
            int middle = start + (end - start) / 2;
            if (arr[middle] == x) {
                start = middle;
                end = middle;
            } else if (arr[middle] > x) {
                end = middle - 1;
            } else {
                start = middle + 1;
            }
        }
        if (start >= arr.size()) {
            start = arr.size() - 1;
        }

        int count = 1;
        if (start - 1 >= 0 && abs(arr[start - 1] - x) < abs(arr[start] - x)) {
            start--;
        } else if (start + 1 < arr.size() && abs(arr[start + 1] - x) < abs(arr[start] - x)) {
            start++;
        }

        end = start;
        while (count < k) {
            if (start > 0 && end < arr.size() - 1) {
                if (abs(arr[start - 1] - x) <= abs(arr[end + 1] - x)) {
                    start--;
                } else {
                    end++;
                }
                count++;
            } else if (start == 0 && end < arr.size() - 1) {
                end++;
                if (abs(arr[start] - x) <= abs(arr[end] - x)) {
                    // remove the right bigger value
                    start++;
                } else {
                    count++;
                }
            } else if (end == arr.size() - 1 && start > 0) {
                start--;
                if (abs(arr[start] - x) <= abs(arr[end] - x)) {
                    // remove the right bigger value
                    end--;
                } else {
                    count++;
                }
            } else {
                break;
            }
        }
        return {arr.begin() + start, arr.begin() + end + 1};
    }
};


int main() {
    Solution s;
    vector<int> array {3,5,8,10};
    auto res = s.findClosestElements(array, 2, 15);
    for (auto &e: res) {
        cout << e << ',';
    }
    cout << endl;
}

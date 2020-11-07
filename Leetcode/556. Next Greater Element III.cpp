#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
#include <unordered_map>
using namespace std;


// Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

// Example 1:

// Input: 12
// Output: 21
 

// Example 2:

// Input: 21
// Output: -1


class Solution {
public:
    int nextGreaterElement(int n) {
        auto array_n = create_int_array(n);
        int size = array_n.size();
        bool found = false;
        for (int i = 0; i < size - 1; i++) {
            if (array_n[i] > array_n[i + 1]) {
                found = true;
                // find the value bigger than array_n[i+1]
                int min_v = INT32_MAX;
                for (int j = 0; j < i + 1; j++) {
                    if (array_n[j] > array_n[i + 1] && array_n[j] < min_v) {
                        min_v = j;
                    }
                }
                swap(array_n[i+1], array_n[min_v]);
                sort(array_n.begin(), array_n.begin() + i + 1, [](int i, int j) {
                    return i > j;
                });
                break;
            }
        }
        return found? form_int(array_n): -1;
    }

    vector<int> create_int_array(int n) {
        vector<int> array;
        while (n) {
            array.push_back(n % 10);
            n /= 10;
        }
        return array;
    }

    int form_int(vector<int> &array) {
        int size = array.size();
        int res = 0;
        int limit = INT32_MAX / 10;
        for (int i = size - 1; i >= 0; i--) {
            res = 10 * res + array[i];
            if (res >= limit) {
                return -1;
            }
        }
        return res;
    }
};

int main() {
    Solution s;
    cout << s.nextGreaterElement(1999999999) << endl;
}
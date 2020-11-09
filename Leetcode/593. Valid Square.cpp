#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
#include <unordered_map>
using namespace std;


// Given the coordinates of four points in 2D space, return whether the four points could construct a square.

// The coordinate (x,y) of a point is represented by an integer array with two integers.

// Example:

// Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
// Output: True
 

// Note:

// All the input integers are in the range [-10000, 10000].
// A valid square has four equal sides with positive length and four equal angles (90-degree angles).
// Input points have no order.


class Solution {
public:
    bool validSquare(vector<int>& p1, vector<int>& p2, vector<int>& p3, vector<int>& p4) {
        int dis_1_to_2 = distance2power(p1, p2);
        int dis_1_to_3 = distance2power(p1, p3);
        int dis_1_to_4 = distance2power(p1, p4);

        if (dis_1_to_2 == 0 || dis_1_to_3 == 0 || dis_1_to_4 == 0) {
            return false;
        } else if (dis_1_to_2 == dis_1_to_3 && dis_1_to_4 == (dis_1_to_2 + dis_1_to_3)) {
            // judge slope
            return is90degree(p2, p1, p3) && is90degree(p2, p4, p3);
        } else if (dis_1_to_2 == dis_1_to_4 && dis_1_to_3 == (dis_1_to_2 + dis_1_to_4)) {
            return is90degree(p2, p1, p4) && is90degree(p2, p3, p4);
        } else if (dis_1_to_3 == dis_1_to_4 && dis_1_to_2 == (dis_1_to_3 + dis_1_to_4)) {
            return is90degree(p3, p1, p4) && is90degree(p3, p2, p4);
        }
        return false;
    }

    int distance2power(vector<int> &a, vector<int> &b) {
        return abs((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]));
    }

    double is90degree(vector<int> &a, vector<int> &b, vector<int> &c) {
        return (b[1] - a[1]) * (b[1] - c[1]) + (b[0] - a[0]) * (b[0] - c[0]) == 0;
    }
};

int main() {
    Solution s;
    vector<int> p1 {0, 0};
    vector<int> p2 {1, 1};
    vector<int> p3 {1, 0};
    vector<int> p4 {0, 1};
    cout << boolalpha << s.validSquare(p1, p2, p3, p4);
}
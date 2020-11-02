#include <unordered_map>
#include <unordered_set>
#include <math.h>
#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;


// Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 

// Example 1:

// Input: timePoints = ["23:59","00:00"]
// Output: 1
// Example 2:

// Input: timePoints = ["00:00","23:59","00:00"]
// Output: 0
 

// Constraints:

// 2 <= timePoints <= 2 * 104
// timePoints[i] is in the format "HH:MM".


class Solution {
public:
    int time2int(string &time) {
        int hour, minute;
        sscanf(time.c_str(), "%d:%d", &hour, &minute);
        return hour * 60 + minute;
    }

    int findMinDifference(vector<string>& timePoints) {
        if (timePoints.size() < 2) {
            return -1;
        }

        vector<int> times;
        for (auto &e: timePoints) {
            times.push_back(time2int(e));
        }

        sort(times.begin(), times.end());

        int min_dis = INT32_MAX;
        int min_v = times[0];
        int max_v = times[0];
        int one_day = 24*60;
        for (int i = 1; i < times.size(); i++) {
            min_dis = min(min_dis, min(times[i] - max_v, one_day - (times[i] - min_v)));
            max_v = times[i];
        }
        return min_dis;
    }
};

int main() {
    Solution s;
    vector<string> array {"23:59","00:00"};
    cout << s.findMinDifference(array) << endl;
}
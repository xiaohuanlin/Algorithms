#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;


// Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

// Note:
// The number of people is less than 1,100.

 
// Example

// Input:
// [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

// Output:
// [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        vector<vector<int>> res;
        if (people.empty()) {
            return res;
        }
        vector<vector<int>> copy_one;
        for (int j = 0; j < people.size(); j++) {
            copy_one.push_back(vector<int>{people[j][0], people[j][1], people[j][1]});
        }

        for (int i = 0; i < people.size(); i++) {
            res.push_back(move(iter(copy_one)));
        }
        return move(res);
    }

    vector<int> iter(vector<vector<int>> &copy_one) {
        int min_value = INT32_MAX;
        int min_index;
        vector<int> answer;
        for (int i = 0; i < copy_one.size(); i++) {
            if (copy_one[i][2] == 0) {
                if (copy_one[i][0] < min_value) {
                    min_value = copy_one[i][0];
                    min_index = i;
                    answer = {copy_one[i][0], copy_one[i][1]};
                }
            }
        }

        // modify values that less then min_value
        for (int j = 0; j < copy_one.size(); j++) {
            if (copy_one[j][0] <= min_value) {
                copy_one[j][2]--;
            }
        }

        copy_one.erase(copy_one.begin() + min_index);
        return move(answer);
    }
};

int main() {
    Solution s;
    vector<vector<int>> array = {
        {7,0}, {4,4}, {7,1}, {5,0}, {6,1}, {5,2}
    };
    auto res = s.reconstructQueue(array);
    for (auto e: res) {
        for (auto l: e) {
            cout << l << ',';
        }
        cout << endl;
    }
}
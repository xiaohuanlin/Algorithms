#include <vector>
#include <queue>
#include <set>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;


// The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

// For example, for arr = [2,3,4], the median is 3.
// For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
// Implement the MedianFinder class:

// MedianFinder() initializes the MedianFinder object.
// void addNum(int num) adds the integer num from the data stream to the data structure.
// double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

// Example 1:

// Input
// ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
// [[], [1], [2], [], [3], []]
// Output
// [null, null, null, 1.5, null, 2.0]

// Explanation
// MedianFinder medianFinder = new MedianFinder();
// medianFinder.addNum(1);    // arr = [1]
// medianFinder.addNum(2);    // arr = [1, 2]
// medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
// medianFinder.addNum(3);    // arr[1, 2, 3]
// medianFinder.findMedian(); // return 2.0
 

// Constraints:

// -105 <= num <= 105
// There will be at least one element in the data structure before calling findMedian.
// At most 5 * 104 calls will be made to addNum and findMedian.
 

// Follow up:

// If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
// If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?


class MedianFinder {
    priority_queue<int, vector<int>, greater<int>> bigger_queue;
    priority_queue<int> smaller_queue;
public:
    MedianFinder() {}
    
    void addNum(int num) {
        if (bigger_queue.size() == smaller_queue.size()) {
            if (bigger_queue.empty() || num >= smaller_queue.top()) {
                // insert it without any effect
                bigger_queue.push(num);
            } else {
                int value = smaller_queue.top();
                smaller_queue.pop();

                smaller_queue.push(num);
                bigger_queue.push(value);
            }
        } else {
            if (smaller_queue.empty() || num <= bigger_queue.top()) {
                // insert it without any effect
                smaller_queue.push(num);
            } else {
                int value = bigger_queue.top();
                bigger_queue.pop();

                bigger_queue.push(num);
                smaller_queue.push(value);
            }
        }

        // sort at first num
        if (bigger_queue.size() == 1 && smaller_queue.size() == 1) {
            int big = bigger_queue.top();
            int small = smaller_queue.top();
            if (big < small) {
                bigger_queue.pop();
                smaller_queue.pop();
                bigger_queue.push(small);
                smaller_queue.push(big);
            }
        }

    }
    
    double findMedian() {
        if (bigger_queue.size() == smaller_queue.size()) {
            return (bigger_queue.top() + smaller_queue.top()) / 2.0;
        } else {
            return bigger_queue.top();
        }
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */

int main() {
    MedianFinder*  medianFinder = new MedianFinder();
    medianFinder->addNum(1);    // arr = [1]
    medianFinder->addNum(2);    // arr = [1, 2]
    assert(medianFinder->findMedian() == 1.5); // return 1.5 (i.e., (1 + 2) / 2)
    medianFinder->addNum(3);    // arr[1, 2, 3]
    assert(medianFinder->findMedian() == 2.0); // return 2.0
}
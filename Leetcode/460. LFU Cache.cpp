#include <vector>
#include <unordered_map>
#include <set>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;


// Design and implement a data structure for a Least Frequently Used (LFU) cache.

// Implement the LFUCache class:

// LFUCache(int capacity) Initializes the object with the capacity of the data structure.
// int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
// void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
// To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

// When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

// The functions get and put must each run in O(1) average time complexity.

 

// Example 1:

// Input
// ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
// [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
// Output
// [null, null, null, 1, null, -1, 3, null, -1, 3, 4]

// Explanation
// // cnt(x) = the use counter for key x
// // cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
// LFUCache lfu = new LFUCache(2);
// lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
// lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
// lfu.get(1);      // return 1
//                  // cache=[1,2], cnt(2)=1, cnt(1)=2
// lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
//                  // cache=[3,1], cnt(3)=1, cnt(1)=2
// lfu.get(2);      // return -1 (not found)
// lfu.get(3);      // return 3
//                  // cache=[3,1], cnt(3)=2, cnt(1)=2
// lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
//                  // cache=[4,3], cnt(4)=1, cnt(3)=2
// lfu.get(1);      // return -1 (not found)
// lfu.get(3);      // return 3
//                  // cache=[3,4], cnt(4)=1, cnt(3)=3
// lfu.get(4);      // return 4
//                  // cache=[3,4], cnt(4)=2, cnt(3)=3
 

// Constraints:

// 0 <= capacity <= 10^4
// 0 <= key <= 10^5
// 0 <= value <= 10^9
// At most 2 * 10^5 calls will be made to get and put.


class LFUCache {
    unordered_map<int, tuple<int, int>> key_to_value_fre_;
    unordered_map<int, vector<int>> fre_to_keys_;
    int min_freq_;
    int size_ = 0;
    int capacity_;

    void change_freq(unordered_map<int, tuple<int, int>>::iterator iter, int key) {
        auto freq = std::get<1>(iter->second)++;
        auto& keys = fre_to_keys_[freq];
        auto keys_iter = find(keys.begin(), keys.end(), key);
        keys.erase(keys_iter);
        // increase minfreq
        if (keys.size() == 0 && freq == min_freq_) {
            min_freq_++;
        }
        fre_to_keys_[freq+1].push_back(key);
    }

public:
    LFUCache(int capacity): capacity_(capacity) {}
    
    int get(int key) {
        auto iter = key_to_value_fre_.find(key);
        if (iter == key_to_value_fre_.end()) {
            return -1;
        }
        change_freq(iter, key);
        return std::get<0>(iter->second);
    }
    
    void put(int key, int value) {
        if (capacity_ == 0) {
            return;
        }

        auto iter = key_to_value_fre_.find(key);
        if (iter != key_to_value_fre_.end()) {
            // for update
            std::get<0>(iter->second) = value;
            change_freq(iter, key);
        } else {
            // for set
            if (++size_ > capacity_) {
                // explicit
                auto& keys = fre_to_keys_[min_freq_];
                auto erase_key = keys.front();
                keys.erase(keys.begin());
                key_to_value_fre_.erase(erase_key);
                size_ = capacity_;
            }

            // insert new element
            fre_to_keys_[1].push_back(key);
            key_to_value_fre_[key] = {value, 1};
            min_freq_ = 1;
        }
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */


int main() {
    LFUCache* obj = new LFUCache(2);
    obj->put(1, 1);
    obj->put(2, 2);
    assert(obj->get(1) == 1);
    obj->put(3, 3);
    assert(obj->get(2) == -1);
    assert(obj->get(3) == 3);
    obj->put(4, 4);
    assert(obj->get(1) == -1);
    assert(obj->get(3) == 3);
}
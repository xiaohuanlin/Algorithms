#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
#include <unordered_map>
#include <cstdlib>
using namespace std;


// Design a data structure that supports all following operations in average O(1) time.

 

// insert(val): Inserts an item val to the set if not already present.
// remove(val): Removes an item val from the set if present.
// getRandom: Returns a random element from current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
 

// Example:

// // Init an empty set.
// RandomizedSet randomSet = new RandomizedSet();

// // Inserts 1 to the set. Returns true as 1 was inserted successfully.
// randomSet.insert(1);

// // Returns false as 2 does not exist in the set.
// randomSet.remove(2);

// // Inserts 2 to the set, returns true. Set now contains [1,2].
// randomSet.insert(2);

// // getRandom should return either 1 or 2 randomly.
// randomSet.getRandom();

// // Removes 1 from the set, returns true. Set now contains [2].
// randomSet.remove(1);

// // 2 was already in the set, so return false.
// randomSet.insert(2);

// // Since 2 is the only number in the set, getRandom always return 2.
// randomSet.getRandom();


class RandomizedSet {
    unordered_map<int, int> maps;
    vector<int> vectors;
public:
    /** Initialize your data structure here. */
    RandomizedSet() {
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        auto item = maps.insert({val, vectors.size()});
        if (item.second) {
            vectors.push_back(val);
        }
        return item.second;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        auto iter = maps.begin();
        if ((iter = maps.find(val)) == maps.end()) {
            return false;
        }

        // change this position to end 
        maps[vectors.back()] = iter->second;

        // find in vector
        swap(vectors[iter->second], vectors.back());
        vectors.pop_back();

        maps.erase(iter);
        return true;
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        return vectors[rand() % vectors.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 */

int main() {
    RandomizedSet* obj = new RandomizedSet();
    obj->insert(3);
    obj->remove(3);
    obj->remove(0);
    obj->insert(3);
    cout << obj->getRandom() << endl;
    obj->remove(0);
}
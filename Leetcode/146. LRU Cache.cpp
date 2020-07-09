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


// Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

// get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
// put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

// The cache is initialized with a positive capacity.

// Follow up:
// Could you do both operations in O(1) time complexity?

// Example:

// LRUCache cache = new LRUCache( 2 /* capacity */ );

// cache.put(1, 1);
// cache.put(2, 2);
// cache.get(1);       // returns 1
// cache.put(3, 3);    // evicts key 2
// cache.get(2);       // returns -1 (not found)
// cache.put(4, 4);    // evicts key 1
// cache.get(1);       // returns -1 (not found)
// cache.get(3);       // returns 3
// cache.get(4);       // returns 4


 
class LRUCache {
private:
    struct ListNode {
        int key;
        int val;
        ListNode* previous;
        ListNode* next;
        ListNode(int k, int v): key(k), val(v), previous(nullptr), next(nullptr) {};
    };

    unordered_map<int, ListNode*> maps;
    ListNode *head, *tail;
    int capacity;

public:
    LRUCache(int capacity): capacity(capacity), head(nullptr), tail(nullptr) {
        maps.reserve(capacity);
    }
    
    int get(int key) {
        if (maps.find(key) == maps.end()) {
            return -1;
        }

        auto node = maps[key];
        if (node == head) {
            head = head->next;
            tail = node;
        }

        if (node == tail) {
            return node->val;
        }

        node->previous->next = node->next;
        node->next->previous = node->previous;

        tail->next = node;
        node->previous = tail;

        node->next = head;
        head->previous = node;

        tail = node;
        return node->val;
    }
    
    void put(int key, int value) {
        if (capacity <= 0) {
            return;
        }

        if (maps.find(key) != maps.end()) {
            get(key);
            tail->val = value;
            return;
        }

        if (maps.size() < capacity) {
            ListNode *node = new ListNode(key, value);
            maps[key] = node;
            if (tail) {
                tail->next = node;
                node->previous = tail;
            } else {
                head = node;
            }
            tail = node;
            tail->next = head;
            head->previous = tail;
        } else {
            maps.erase(head->key);
            head->key = key;
            head->val = value;
            maps[key] = head;

            tail = head;
            head = head->next;
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */

int main() {
    LRUCache* cache = new LRUCache(10);

    cache->put(10, 13);
    cache->put(3, 17);
    cache->put(6, 11);
    cache->put(10, 5);
    cache->put(9, 10);
    cout << cache->get(13) << endl;
    cache->put(2, 19);
    cout << cache->get(2) << endl;
    cout << cache->get(3) << endl;
    cache->put(5, 25);
    cout << cache->get(8) << endl;
    cache->put(9, 22);
    cache->put(5, 5);
    cache->put(1, 30);
    cout << cache->get(11) << endl;
    cache->put(9, 12);
    cout << cache->get(7) << endl;
    cout << cache->get(5) << endl;
    cout << cache->get(8) << endl;
    cout << cache->get(9) << endl;
    cache->put(4, 30);
    cache->put(9, 3);
    cout << cache->get(9) << endl;
    cout << cache->get(10) << endl;
    cout << cache->get(10) << endl;
    cache->put(6, 14);
    cache->put(3, 1);
    cout << cache->get(3) << endl;
    cache->put(10, 11);
    cout << cache->get(8) << endl;
    cache->put(2, 14);
    cout << cache->get(1) << endl;
    cout << cache->get(5) << endl;
    cout << cache->get(4) << endl;
    cache->put(11, 4);
    cache->put(12, 24);
    cache->put(5, 18);
    cout << cache->get(13) << endl;
    cache->put(7, 23);
    cout << cache->get(8) << endl;
    cout << cache->get(12) << endl;
    cache->put(3, 27);
    cache->put(2, 12);
    cout << cache->get(5) << endl;
    cache->put(2, 9);
    cache->put(13, 4);
    cache->put(8, 18);
    cache->put(1, 7);
    cout << cache->get(6) << endl;
    cache->put(9, 29);
    cache->put(8, 21);
    cout << cache->get(5) << endl;
    cache->put(6, 30);
    cache->put(1, 12);
    cout << cache->get(10) << endl;
    cache->put(4, 15);
    cache->put(7, 22);
    cache->put(11, 26);
    cache->put(8, 17);
    cache->put(9, 29);
    cout << cache->get(5) << endl;
    cache->put(3, 4);
    cache->put(11, 30);
    cout << cache->get(12) << endl;
    cache->put(4, 29);
    cout << cache->get(3) << endl;
    cout << cache->get(9) << endl;
    cout << cache->get(6) << endl;
    cache->put(3, 4);
    cout << cache->get(1) << endl;
    cout << cache->get(10) << endl;
    cache->put(3, 29);
    cache->put(10, 28);
    cache->put(1, 20);
    cache->put(11, 13);
    cout << cache->get(3) << endl;
    cache->put(3, 12);
    cache->put(3, 8);
    cache->put(10, 9);
    cache->put(3, 26);
    cout << cache->get(8) << endl;
    cout << cache->get(7) << endl;
    cout << cache->get(5) << endl;
    cache->put(13, 17);
    cache->put(2, 27);
    cache->put(11, 15);
    cout << cache->get(12) << endl;
    cache->put(9, 19);
    cache->put(2, 15);
    cache->put(3, 16);
    cout << cache->get(1) << endl;
    cache->put(12, 17);
    cache->put(9, 1);
    cache->put(6, 19);
    cout << cache->get(4) << endl;
    cout << cache->get(5) << endl;
    cout << cache->get(5) << endl;
    cache->put(8, 1);
    cache->put(11, 7);
    cache->put(5, 2);
    cache->put(9, 28);
    cout << cache->get(1) << endl;
    cache->put(2, 2);
    cache->put(7, 4);
    cache->put(4, 22);
    cache->put(7, 24);
    cache->put(9, 26);
    cache->put(13, 28);
    cache->put(11, 26);
}

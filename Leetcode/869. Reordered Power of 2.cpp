#include <vector>
#include <array>
#include <tuple>
#include <assert.h>
#include <algorithm>
using namespace std;

// You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

// Return true if and only if we can do this so that the resulting number is a power of two.

 

// Example 1:

// Input: n = 1
// Output: true
// Example 2:

// Input: n = 10
// Output: false
// Example 3:

// Input: n = 16
// Output: true
// Example 4:

// Input: n = 24
// Output: false
// Example 5:

// Input: n = 46
// Output: true
 

// Constraints:

// 1 <= n <= 109

class Solution {
public:
    using Length = int;
    // using Item = pair<Length, int[10]>;
    class Item {
    public:
        Length length_ = 0;
        int counts_[10] {};
    };

    bool reorderedPowerOf2(int n) {
        // 10^9 < 2^32
        Item two_power_res[32];
        int64_t res = 1;
        for (int i = 0; i < 32; i++) {
            initItem(&two_power_res[i], res);
            res *= 2;
        }

        Item n_item;
        initItem(&n_item, n);

        for (int i = 0; i < 32; i++) {
            if (equalItem(n_item, two_power_res[i])) {
                return true;
            }
        }
        return false;
    }

    void initItem(Item* item, int64_t value) {
        string value_str = to_string(value);
        item->length_ = value_str.length();
        for (auto& c : value_str) {
            item->counts_[c - '0']++;
        }
        return;
    }

    bool equalItem(const Item& a, const Item& b) {
        if (a.length_ != b.length_) {
            return false;
        }
        for (int i = 0; i < 10; i++) {
            if (a.counts_[i] != b.counts_[i]) {
                return false;
            }
        }
        return true;
    }
};

int main() {
    Solution s;
    vector<tuple<int, bool>> test_cases {
        {1, true},
        {10, false},
        {16, true},
        {24, false},
        {46, true},
    };

    for (auto& test_case: test_cases) {
        assert(s.reorderedPowerOf2(get<0>(test_case)) == get<1>(test_case));
    }
}
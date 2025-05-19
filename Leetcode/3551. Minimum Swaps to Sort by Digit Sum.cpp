#include <vector>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <functional>
#include <type_traits>
#include <iterator>
#include <utility>
using namespace std;

template <typename T>
class is_container
{
   private:
    template <typename C>
    static auto check(C* c) -> decltype(begin(*c), end(*c), typename C::iterator{},
                                        typename C::value_type{}, true_type{});

    static constexpr false_type check(...);

   public:
    static constexpr bool value = decltype(check(static_cast<T*>(nullptr)))::value;
};

template <typename T>
class is_tuple
{
   public:
    static constexpr bool value = false;
};

template <typename... T>
class is_tuple<tuple<T...>>
{
   public:
    static constexpr bool value = true;
};

template <typename T>
class is_streamable
{
   private:
    template <typename C>
    static auto check(C* c) -> decltype(void(declval<ostream&>() << declval<C>()), true_type{});
    static constexpr false_type check(...);

   public:
    static constexpr bool value = decltype(check(static_cast<T*>(nullptr)))::value;
};

template <typename T>
void print(const T& t)
{
    if constexpr (is_container<T>::value)
    {
        cout << "[";
        for (auto&& it = t.begin(); it != t.end(); ++it)
        {
            print(*it);
            if (next(it) != t.end())
            {
                cout << ", ";
            }
        }
        cout << "]";
    }
    else if constexpr (is_tuple<T>::value)
    {
        cout << "(";
        [&t]<size_t... I>(index_sequence<I...>)
        { (print(get<I>(t)), ...); }(make_index_sequence<tuple_size<T>::value>{});
        cout << ")";
    }
    else if constexpr (is_streamable<T>::value)
    {
        cout << t;
    }
    else
    {
    }
}

// You are given an array nums of distinct positive integers. You need to sort the array in increasing order based on the sum of the digits of each number. If two numbers have the same digit sum, the smaller number appears first in the sorted order.

// Return the minimum number of swaps required to rearrange nums into this sorted order.

// A swap is defined as exchanging the values at two distinct positions in the array.

// Example 1:

// Input: nums = [37,100]

// Output: 1

// Explanation:

// Compute the digit sum for each integer: [3 + 7 = 10, 1 + 0 + 0 = 1] → [10, 1]
// Sort the integers based on digit sum: [100, 37]. Swap 37 with 100 to obtain the sorted order.
// Thus, the minimum number of swaps required to rearrange nums is 1.
// Example 2:

// Input: nums = [22,14,33,7]

// Output: 0

// Explanation:

// Compute the digit sum for each integer: [2 + 2 = 4, 1 + 4 = 5, 3 + 3 = 6, 7 = 7] → [4, 5, 6, 7]
// Sort the integers based on digit sum: [22, 14, 33, 7]. The array is already sorted.
// Thus, the minimum number of swaps required to rearrange nums is 0.
// Example 3:

// Input: nums = [18,43,34,16]

// Output: 2

// Explanation:

// Compute the digit sum for each integer: [1 + 8 = 9, 4 + 3 = 7, 3 + 4 = 7, 1 + 6 = 7] → [9, 7, 7, 7]
// Sort the integers based on digit sum: [16, 34, 43, 18]. Swap 18 with 16, and swap 43 with 34 to obtain the sorted order.
// Thus, the minimum number of swaps required to rearrange nums is 2.

// Constraints:

// 1 <= nums.length <= 105
// 1 <= nums[i] <= 109
// nums consists of distinct positive integers.

class Solution
{
   public:
    int getSum(int value)
    {
        int res = 0;
        while (value)
        {
            res += value % 10;
            value /= 10;
        }
        return res;
    }

    int minSwaps(vector<int>& nums)
    {
        vector<vector<int>> l(nums.size(), vector<int>(3, 0));
        vector<vector<int>> m(nums.size(), vector<int>(3, 0));
        for (auto i = 0; i < nums.size(); i++)
        {
            l[i][0] = getSum(nums[i]);
            l[i][1] = nums[i];
            l[i][2] = i;
            m[i][0] = getSum(nums[i]);
            m[i][1] = nums[i];
            m[i][2] = i;
        }
        sort(l.begin(), l.end());
        int res = 0;
        unordered_map<int,int> maps;
        for (auto i = 0; i < nums.size(); i++)
        {
            auto& idx = m[i][2];
            auto& sorted_idx = l[i][2];
            maps[idx] = sorted_idx;
        }

        unordered_set<int> visited;
        for (auto i = 0; i < nums.size(); i++) {
            if (visited.find(i) != visited.end()) {
                continue;
            }
            auto iter = i;
            visited.insert(iter);
            int len = 0;
            while (i != maps[iter]) {
                iter = maps[iter];
                visited.insert(iter);
                len += 1;
            }
            res += len;
        }
        return res;
    }
};


int main()
{
    Solution s;
    vector<pair<tuple<Solution, vector<int>>, int>> test_cases{
        {{s, {2233542, 122244, 32112433, 37, 65324, 772, 111, 45462, 56783}}, 6},
        // {{s, {37, 100}}, 1},
        // {{s, {22, 14, 33, 7}}, 0},
        // {{s, {18, 43, 34, 16}}, 2},
    };

    for (auto&& [params, result] : test_cases)
    {
        if (auto res = apply(&Solution::minSwaps, params); res != result)
        {
            cout << "Test failed: " << res << " != " << result << endl;
            cout << "Input: ";
            print(params);
            cout << endl;
        }
    }
}
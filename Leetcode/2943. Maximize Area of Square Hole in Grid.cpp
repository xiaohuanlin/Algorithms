#include <vector>
#include <stack>
#include <unordered_map>
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
        cout << t << ", ";
    }
    else
    {
    }
}

// You are given the two integers, n and m and two integer arrays, hBars and vBars. The grid has n + 2 horizontal and m + 2 vertical bars, creating 1 x 1 unit cells. The bars are indexed starting from 1.

// You can remove some of the bars in hBars from horizontal bars and some of the bars in vBars from vertical bars. Note that other bars are fixed and cannot be removed.

// Return an integer denoting the maximum area of a square-shaped hole in the grid, after removing some bars (possibly none).

// Example 1:

// Input: n = 2, m = 1, hBars = [2,3], vBars = [2]

// Output: 4

// Explanation:

// The left image shows the initial grid formed by the bars. The horizontal bars are [1,2,3,4], and the vertical bars are [1,2,3].

// One way to get the maximum square-shaped hole is by removing horizontal bar 2 and vertical bar 2.

// Example 2:

// Input: n = 1, m = 1, hBars = [2], vBars = [2]

// Output: 4

// Explanation:

// To get the maximum square-shaped hole, we remove horizontal bar 2 and vertical bar 2.

// Example 3:

// Input: n = 2, m = 3, hBars = [2,3], vBars = [2,4]

// Output: 4

// Explanation:

// One way to get the maximum square-shaped hole is by removing horizontal bar 3, and vertical bar 4.

// Constraints:

// 1 <= n <= 109
// 1 <= m <= 109
// 1 <= hBars.length <= 100
// 2 <= hBars[i] <= n + 1
// 1 <= vBars.length <= 100
// 2 <= vBars[i] <= m + 1
// All values in hBars are distinct.
// All values in vBars are distinct.

class Solution
{
   public:
    int get_max_intervals(int total, vector<int>& bars)
    {
        sort(bars.begin(), bars.end());
        int maxhv = -1;
        for (int i = 0; i < bars.size();)
        {
            int j = i + 1;
            while (j < bars.size() && bars[j] - bars[j - 1] == 1)
            {
                j++;
            }
            maxhv = max(maxhv, j - i + 1);
            i = j;
        }
        return maxhv;
    }

    int maximizeSquareHoleArea(int n, int m, vector<int>& hBars, vector<int>& vBars)
    {
        int v = min(get_max_intervals(n + 2, hBars), get_max_intervals(m + 2, vBars));
        return v * v;
    }
};

int main()
{
    Solution s;
    vector<pair<tuple<Solution, int, int, vector<int>, vector<int>>, int>> test_cases{
        {{s, 2, 1, {2, 3}, {2}}, 4},
        {{s, 1, 1, {2}, {2}}, 4},
        {{s, 2, 3, {2, 3}, {2, 4}}, 4},
    };

    for (auto&& [params, result] : test_cases)
    {
        if (auto res = apply(&Solution::maximizeSquareHoleArea, params); res != result)
        {
            cout << "Test failed: " << res << " != " << result << endl;
            cout << "Input: ";
            print(params);
            cout << endl;
        }
    }
}
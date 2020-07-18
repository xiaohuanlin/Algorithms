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


// Write a program to find the nth super ugly number.

// Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

// Example:

// Input: n = 12, primes = [2,7,13,19]
// Output: 32 
// Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
//              super ugly numbers given primes = [2,7,13,19] of size 4.
// Note:

// 1 is a super ugly number for any given primes.
// The given numbers in primes are in ascending order.
// 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
// The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
		if (primes.empty()) {
			return -1;
		}

		vector<int> points(primes.size(), 0);
		vector<int> res(n, 1);
		int count = 1;

		while (count < n) {
			int min_value = INT32_MAX;
			int min_prime;
			for (int j = 0; j < primes.size(); j++) {
				if (res[points[j]] * primes[j] < min_value) {
					min_value = res[points[j]] * primes[j];
					min_prime = j;
				}
			}

			points[min_prime]++;
			if (min_value == res[count-1]) {
				continue;
			}

			res[count++] = min_value;
		}

		return res.back();
    }
};

int main() {
	Solution s;
	vector<int> array = {2,7,13,19};
	cout << s.nthSuperUglyNumber(12, array);
}
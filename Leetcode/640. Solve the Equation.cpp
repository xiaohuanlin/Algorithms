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
#include <queue>
using namespace std;


// Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

// If there is no solution for the equation, return "No solution".

// If there are infinite solutions for the equation, return "Infinite solutions".

// If there is exactly one solution for the equation, we ensure that the value of x is an integer.

// Example 1:
// Input: "x+5-3+x=6+x-2"
// Output: "x=2"
// Example 2:
// Input: "x=x"
// Output: "Infinite solutions"
// Example 3:
// Input: "2x=x"
// Output: "x=0"
// Example 4:
// Input: "2x+3x-6x=x+2"
// Output: "x=-1"
// Example 5:
// Input: "x=x+2"
// Output: "No solution"




class Solution {
public:
    string solveEquation(string equation) {
        long x_count = 0;
        long value_count = 0;        
        int count = 0;

        long delta = 1;
        while (count < equation.size()) {
            switch (equation[count])
            {
                case '=': {
                    delta = -1;
                    count++;
                    break;
                }
                case '+': {
                    count++;
                    if (equation[count] == 'x') {
                        x_count += delta;
                        count++;
                    } else {
                        long value = delta * (load_number(equation, count));
                        if (count < equation.size() && equation[count] == 'x') {
                            x_count += value;
                            count++;
                        } else {
                            value_count += value;
                        }
                    }
                    break;
                }
                case '-': {
                    count++;
                    if (equation[count] == 'x') {
                        x_count -= delta;
                        count++;
                    } else {
                        long value = delta * (load_number(equation, count));
                        if (count < equation.size() && equation[count] == 'x') {
                            x_count -= value;
                            count++;
                        } else {
                            value_count -= value;
                        }
                    }
                    break;
                }
                default:
                    if (equation[count] == 'x') {
                        x_count += delta;
                        count++;
                    } else {
                        long value = delta * (load_number(equation, count));
                        if (count < equation.size() && equation[count] == 'x') {
                            x_count += value;
                            count++;
                        } else {
                            value_count += value;
                        }
                    }
                    break;
            }
        }

        if (x_count == 0) {
            if (value_count == 0) {
                return "Infinite solutions";
            } else {
                return "No solution";
            }
        }
        return "x=" + to_string(value_count * (-1) / x_count);
    }

    long load_number(string &s, int &iter) {
        int start = iter;
        while (iter < s.size() && s[iter] >= '0' && s[iter] <= '9') {
            iter++;
        }
        return atol(s.substr(start, iter-start).c_str());
    }
};

int main() {
    Solution s;
    cout << s.solveEquation("2x+0=0") << endl;
}

#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

// Example 1:

// Input: num1 = "2", num2 = "3"
// Output: "6"
// Example 2:

// Input: num1 = "123", num2 = "456"
// Output: "56088"
// Note:

// The length of both num1 and num2 is < 110.
// Both num1 and num2 contain only digits 0-9.
// Both num1 and num2 do not contain any leading zero, except the number 0 itself.
// You must not use any built-in BigInteger library or convert the inputs to integer directly.


char maps[] = {'0','1','2','3','4','5','6','7','8','9'};
class Solution {
public:
    string convert_to_string(unsigned int value) {
        if (value == 0) {
            return "0";
        }
        vector<char> res;
        while (value > 0) {
            res.push_back(maps[value % 10]);
            value /= 10;
        }
        reverse(res.begin(), res.end());
        return string(res.begin(), res.end());
    }

    string add(const string &n1, const string &n2) {
        int carry = 0;
        int store = 0;
        int n1_length = n1.length();
        int n2_length = n2.length();
        int max_length = n1_length > n2_length ? n1_length + 1: n2_length + 1;

        string res(max_length, '0');
        while (n1_length > 0 && n2_length > 0) {
            store = (n1[--n1_length] - '0') + (n2[--n2_length] - '0') + carry;
            carry = store / 10;
            res[--max_length] = maps[store % 10];
        }
        while (n1_length > 0) {
            store = (n1[--n1_length] - '0') + carry;
            carry = store / 10;
            res[--max_length] = maps[store % 10];
        }
        while (n2_length > 0) {
            store = (n2[--n2_length] - '0') + carry;
            carry = store / 10;
            res[--max_length] = maps[store % 10];
        }

        if (carry > 0) {
            res[0] = maps[carry];
        } else {
            res = res.substr(1);
        }
        return res;
    }
    
    string multiply(string num1, string num2) {
        if (num1.length() == 1 && num2.length() == 1) {
            return string(convert_to_string((num1[0] - '0') * (num2[0] - '0')));
        }

        string divide_num;
        string divisor_num;
        if (num1.length() > 1) {
            divide_num = num1; 
            divisor_num = num2;
        } else {
            divide_num = num2;
            divisor_num = num1;
        }

        int middle_index = divide_num.size() / 2;
        string left = multiply(divide_num.substr(0, middle_index), divisor_num);
        string right = multiply(divide_num.substr(middle_index), divisor_num);
        if (left != "0") {
            left.append(string(divide_num.length() - middle_index, '0'));
        }
        string res = add(left, right);
        return res;
    }
};


int main() {
    Solution s;
    vector<int> array = {};
    auto res = s.multiply("11110", "0");
    cout << res;
}
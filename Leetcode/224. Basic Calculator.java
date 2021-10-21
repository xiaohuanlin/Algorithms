import java.util.Stack;

// Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

// Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

// Example 1:

// Input: s = "1 + 1"
// Output: 2
// Example 2:

// Input: s = " 2-1 + 2 "
// Output: 3
// Example 3:

// Input: s = "(1+(4+5+2)-3)+(6+8)"
// Output: 23
 

// Constraints:

// 1 <= s.length <= 3 * 105
// s consists of digits, '+', '-', '(', ')', and ' '.
// s represents a valid expression.
// '+' is not used as a unary operation.
// '-' could be used as a unary operation and in this case, it will not be used directly after a +ve or -ve signs (will be inside parentheses).
// There will be no two consecutive operators in the input.
// Every number and running calculation will fit in a signed 32-bit integer.


class Solution224 {
    public int calculate(String s) {
        Stack<Integer> numbers = new Stack<>();

        int result = 0;
        int number = 0;
        int sign = 1;
        for (int start = 0; start < s.length(); start++) {
            char c = s.charAt(start);
            if (c == ')') {
                int right = numbers.pop() * (result + sign * number);
                result = numbers.pop() + right;
                number = 0;
                sign = 1;
            } else if (c == '(') {
                numbers.push(result);
                numbers.push(sign);
                result = 0;
                number = 0;
                sign = 1;
            } else if (c == '+') {
                result += sign * number;
                sign = 1;
                number = 0;
            } else if (c == '-') {
                result += sign * number;
                sign = -1;
                number = 0;
            } else if (Character.isDigit(c)) {
                number = 10 * number + c - '0';
            }
        }

        result += sign * number;

        return result;
    }
}

class Driver224 {
    public static void main(String[] args) {
        Solution224 solution = new Solution224();
        
        String s = "(1+(4+5+2)-3)+(6+8)";
        System.out.println(solution.calculate(s));
    }
}
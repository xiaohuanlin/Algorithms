'''

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
'''
import unittest


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, n+1):
            three_status, five_status = (i % 3 == 0, i % 5 == 0)
            if three_status and not five_status:
                word = 'Fizz'
            elif three_status and five_status:
                word = 'FizzBuzz'
            elif not three_status and five_status:
                word = 'Buzz'
            else:
                word = str(i)
            result.append(word)
        return result


class TestSolution(unittest.TestCase):

    def test_fizzBuzz(self):
        examples = (
            (15, [
                    "1",
                    "2",
                    "Fizz",
                    "4",
                    "Buzz",
                    "Fizz",
                    "7",
                    "8",
                    "Fizz",
                    "Buzz",
                    "11",
                    "Fizz",
                    "13",
                    "14",
                    "FizzBuzz"
                ]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().fizzBuzz(first), second, msg="first: {}; second: {}".format(first, second))


unittest.main()
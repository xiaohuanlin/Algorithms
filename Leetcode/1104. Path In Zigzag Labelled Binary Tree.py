'''
In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.



Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.

 

Example 1:

Input: label = 14
Output: [1,3,4,14]
Example 2:

Input: label = 26
Output: [1,2,6,10,26]
 

Constraints:

1 <= label <= 10^6
'''
from typing import *

import unittest


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        # build list
        last_label_every_row = []
        current = 1
        while current < 2 * 1e6:
            last_label_every_row.append(current)
            current = current * 2 + 1

        def find_op(num):
            if num == 1:
                return 1
            for i in range(len(last_label_every_row)):
                if last_label_every_row[i] >= num:
                    return last_label_every_row[i] + last_label_every_row[i - 1] + 1 - num
            return -1

        while label != 1:
            res.append(label)
            label = find_op(label // 2)
        res.append(1)
        return res[::-1]


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((14, ), [1,3,4,14]),
            ((26, ), [1,2,6,10,26])
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().pathInZigZagTree(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

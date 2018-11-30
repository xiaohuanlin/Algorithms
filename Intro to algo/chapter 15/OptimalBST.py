import unittest
import unittest.mock
import io
from pprint import pprint


def optimal_bst(p, q):
    """
    :param p: the probability of node
    :param q: the probability of leave node, which means miss the hit
    :return: expect_value, root_table
    """
    leave_node_length = len(q)
    expect_value = [[float('-inf')] * leave_node_length for _ in range(leave_node_length)]
    child_tree_p = [[float('-inf')] * leave_node_length for _ in range(leave_node_length)]
    root_table = [[None] * leave_node_length for _ in range(leave_node_length)]

    # initial data
    for i in range(leave_node_length):
        expect_value[i][i] = q[i]
        child_tree_p[i][i] = q[i]
        root_table[i][i] = i

    for length in range(2, leave_node_length + 1):
        for start in range(leave_node_length - length + 1):
            end = start + length - 1
            expect_value[start][end] = float('+inf')
            child_tree_p[start][end] = child_tree_p[start][end-1] + p[end] + q[end]
            for point in range(start, end):
                min_value = expect_value[start][point] + expect_value[point+1][end] + child_tree_p[start][end]
                if min_value < expect_value[start][end]:
                    expect_value[start][end] = round(min_value, 2)
                    root_table[start][end] = point + 1
    return expect_value, root_table


# def print_bst(root_table, parent, start, end):
#     root_point = root_table[start][end]
#     category = 'p' if start != end else 'q'
#
#     root_name = category + root_point
#
#     if parent is None:
#         # show the root information
#         print('{} is the root'.format(root_name))
#     elif int(root_point[1:]) < int(parent[1:]):
#         print('{} is the left child of {}'.format(root_name, parent))
#     else:
#         print('{} is the right child of {}'.format(root_name, parent))
#
    # if category != 'q' and start <= root_point - 1:
    #     print_bst(root_table, root_name, start, root_point-1)
    # if category != 'q' and root_point <= end:
    #     print_bst(root_table, root_name, root_point, end)


def print_bst(root_table):
    start, end = 0, len(root_table[0])-1
    parent = None
    stack = [(start, end, parent)]

    while stack:
        start, end, parent = stack.pop()
        root_point = root_table[start][end]
        category = 'p' if start != end else 'q'

        root_name = category + str(root_point)

        if parent is None:
            # show the root information
            print('{} is the root'.format(root_name))
        elif int(root_name[1:]) < int(parent[1:]):
            print('{} is the left child of {}'.format(root_name, parent))
        else:
            print('{} is the right child of {}'.format(root_name, parent))

        if category != 'q' and start <= root_point-1:
            stack.append((start, root_point-1, root_name))
        if category != 'q' and root_point <= end:
            stack.append((root_point, end, root_name))


class TestSolution(unittest.TestCase):

    def test_optimal_bst(self):
        examples = (
            (([0, 0.15, 0.1, 0.05, 0.1, 0.2],
              [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]),
             ([[0.05, 0.45, 0.9, 1.25, 1.75, 2.75],
               [float('-inf'), 0.1, 0.4, 0.7, 1.2, 2.0],
               [float('-inf'), float('-inf'), 0.05, 0.25, 0.6, 1.3],
               [float('-inf'), float('-inf'), float('-inf'), 0.05, 0.3, 0.9],
               [float('-inf'), float('-inf'), float('-inf'), float('-inf'), 0.05, 0.5],
               [float('-inf'), float('-inf'), float('-inf'), float('-inf'), float('-inf'), 0.1]],
              [[0, 1, 1, 2, 2, 2],
               [None, 1, 2, 2, 2, 4],
               [None, None, 2, 3, 4, 5],
               [None, None, None, 3, 4, 5],
               [None, None, None, None, 4, 5],
               [None, None, None, None, None, 5]]
              )),
            (([0, 0.04, 0.06, 0.08, 0.02, 0.10, 0.12, 0.14],
              [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05]),
             ([[0.06, 0.28, 0.62, 1.02, 1.34, 1.83, 2.44, 3.12],
              [float('-inf'), 0.06, 0.3, 0.68, 0.93, 1.41, 1.96, 2.61],
              [float('-inf'), float('-inf'), 0.06, 0.32, 0.57, 1.04, 1.48, 2.13],
              [float('-inf'), float('-inf'), float('-inf'), 0.06, 0.24, 0.57, 1.01, 1.55],
              [float('-inf'), float('-inf'), float('-inf'), float('-inf'), 0.05, 0.3, 0.72, 1.2],
              [float('-inf'), float('-inf'), float('-inf'), float('-inf'), float('-inf'), 0.05, 0.32, 0.78],
              [float('-inf'), float('-inf'), float('-inf'), float('-inf'), float('-inf'), float('-inf'), 0.05, 0.34],
              [float('-inf'), float('-inf'), float('-inf'), float('-inf'), float('-inf'), float('-inf'), float('-inf'), 0.05]],
             [[0, 1, 2, 2, 2, 3, 3, 5],
              [None, 1, 2, 3, 3, 3, 5, 5],
              [None, None, 2, 3, 3, 4, 5, 5],
              [None, None, None, 3, 4, 5, 5, 6],
              [None, None, None, None, 4, 5, 6, 6],
              [None, None, None, None, None, 5, 6, 7],
              [None, None, None, None, None, None, 6, 7],
              [None, None, None, None, None, None, None, 7]])
             )
        )
        for first, second in examples:
            self.assert_optimal_bst(first, second)

    def assert_optimal_bst(self, first, second):
        self.assertEqual(optimal_bst(*first), second,
                         msg="first: {}; second: {}".format(first, second))

    def test_print_bst(self):
        examples = (
            (([0, 0.15, 0.1, 0.05, 0.1, 0.2],
              [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]),
             'p2 is the root\n'
             'p5 is the right child of p2\n'
             'q5 is the right child of p5\n'
             'p4 is the left child of p5\n'
             'q4 is the right child of p4\n'
             'p3 is the left child of p4\n'
             'q3 is the right child of p3\n'
             'q2 is the left child of p3\n'
             'p1 is the left child of p2\n'
             'q1 is the right child of p1\n'
             'q0 is the left child of p1\n'
             ),
            (([0, 0.04, 0.06, 0.08, 0.02, 0.10, 0.12, 0.14],
              [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05]),
             'p5 is the root\n'
             'p7 is the right child of p5\n'
             'q7 is the right child of p7\n'
             'p6 is the left child of p7\n'
             'q6 is the right child of p6\n'
             'q5 is the left child of p6\n'
             'p2 is the left child of p5\n'
             'p3 is the right child of p2\n'
             'p4 is the right child of p3\n'
             'q4 is the right child of p4\n'
             'q3 is the left child of p4\n'
             'q2 is the left child of p3\n'
             'p1 is the left child of p2\n'
             'q1 is the right child of p1\n'
             'q0 is the left child of p1\n'
             )
        )
        for first, second in examples:
            self.assert_print_bst(first, second)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_print_bst(self, first, second, mock_stdout=None):
        print_bst(optimal_bst(*first)[1])
        self.assertEqual(mock_stdout.getvalue(), second)


unittest.main()

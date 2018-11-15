import unittest

class Matrix:
    def __init__(self, X):
        self.X = X
        self.size = len(X)

    @property
    def left_top(self):
        return Matrix([self.X[i][:self.size//2] for i in range(self.size//2)])

    @property
    def right_top(self):
        return Matrix([self.X[i][self.size//2:] for i in range(self.size//2)])

    @property
    def left_bottem(self):
        return Matrix([self.X[i][:self.size//2] for i in range(self.size//2, self.size)])

    @property
    def right_bottem(self):
        return Matrix([self.X[i][self.size//2:] for i in range(self.size//2, self.size)])

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.size != other.size:
                raise ValueError('Size not match')
            return Matrix([[row_a[i] + row_b[i] for i in range(self.size)] for row_a, row_b in zip(self.X, other.X)])
        else:
            raise NotImplemented

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.size != other.size:
                raise ValueError('Size not match')
            return Matrix([[row_a[i] - row_b[i] for i in range(self.size)] for row_a, row_b in zip(self.X, other.X)])
        else:
            raise NotImplemented

    def __eq__(self, other):
        if isinstance(other, Matrix):
            if self.size != other.size:
                raise ValueError('Size not match')
            return all(row_a[i] == row_b[i] for row_a, row_b in zip(self.X, other.X) for i in range(self.size))
        else:
            return False

    def __repr__(self):
        return '{}:{}'.format(self.__class__.__name__, self.X)


def multiply_matrix(A, B):
    '''
    :param A: [[num]]
    :param B: [[num]]
    :return: [[num]]
    the matrix have n * n size
    '''
    A = Matrix(A)
    B = Matrix(B)
    n = A.size

    if n == 1:
        return Matrix([[A.X[0][0] * B.X[0][0]]])
    else:
        S_1 = B.right_top - B.right_bottem
        S_2 = A.left_top + A.right_top
        S_3 = A.left_bottem + A.right_bottem
        S_4 = B.left_bottem - B.left_top
        S_5 = A.left_top + A.right_bottem
        S_6 = B.left_top + B.right_bottem
        S_7 = A.right_top - A.right_bottem
        S_8 = B.left_bottem + B.right_bottem
        S_9 = A.left_top - A.left_bottem
        S_10 = B.left_top + B.right_top

        P_1 = multiply_matrix(A.left_top.X, S_1.X)
        P_2 = multiply_matrix(S_2.X, B.right_bottem.X)
        P_3 = multiply_matrix(S_3.X, B.left_top.X)
        P_4 = multiply_matrix(A.right_bottem.X, S_4.X)
        P_5 = multiply_matrix(S_5.X, S_6.X)
        P_6 = multiply_matrix(S_7.X, S_8.X)
        P_7 = multiply_matrix(S_9.X, S_10.X)

        C_left_top = (P_5 + P_4 - P_2 + P_6).X
        C_right_top = (P_1 + P_2).X
        C_left_bottem = (P_3 + P_4).X
        C_right_bottem = (P_5 + P_1 - P_3 - P_7).X

        C_left = C_left_top + C_left_bottem
        C_right = C_right_top + C_right_bottem

        return Matrix([C_left[i] + C_right[i] for i in range(n)])


class TestSolution(unittest.TestCase):

    def test_matrix(self):
        self.assertEqual(Matrix([[1]]) + Matrix([[2]]), Matrix([[3]]))
        self.assertEqual(Matrix([[5, 1], [2, 3]]) - Matrix([[3, 1], [2, 2]]), Matrix([[2, 0], [0, 1]]))


    def test_case(self):
        examples = (
            (([[1]], [[2]]), [[2]]),
            (([[1, 2],
               [3, 4]], [[4, 3],
                         [2, 1]]), [[8, 5],
                                    [20, 13]]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(multiply_matrix(*first), Matrix(second),
                         msg="first: {}; second: {}".format(first, second))



unittest.main()

import unittest

def brute_force_maximum_subarray(nums, low, high):
    max_nums = nums[low]
    max_range = 0, 1
    for i in range(low, high):
        j = i
        max_j = j
        sum_total, max_total = 0, nums[j]
        while j < high:
            sum_total += nums[j]
            if sum_total > max_total:
                max_total = sum_total
                max_j = j
            j += 1
        if max_total > max_nums:
            max_nums = max_total
            max_range = i, max_j
    return (*max_range, max_nums)

def incr_maximum_subarray(nums, low, high):
    # this method is O(n)
    max_sum = nums[low]
    start = 0
    left_index = 0
    end = 1
    sum_value = 0
    for i in range(low, high):
        sum_value += nums[i]
        if sum_value < 0:
            # clear the result, because it can't be a maximum value
            sum_value = 0
            left_index = i + 1
        else:
            if sum_value > max_sum:
                max_sum = sum_value
                start = left_index
                end = i
    return start, end, max_sum


def maximum_subarray(nums, low, high):
    if high - low == 1:
        return low, high, nums[low]
    middle = (low + high) // 2

    left_record = maximum_subarray(nums, low, middle)
    right_record = maximum_subarray(nums, middle, high)
    cross_record = get_middle_subarray(nums, middle)

    return max(left_record, right_record, cross_record, key=lambda x: x[2])


def get_middle_subarray(nums, m):

    sum_left, sum_right = 0, 0
    max_left, max_left_index = nums[m], m
    for i in range(m, -1, -1):
        sum_left += nums[i]
        if sum_left > max_left:
            max_left = sum_left
            max_left_index = i
    if m+1 < len(nums):
        max_right, max_right_index = nums[m+1], m+1
        for i in range(m+1, len(nums)):
            sum_right += nums[i]
            if sum_right > max_right:
                max_right = sum_right
                max_right_index = i
    else:
        max_right_index = m
        max_right = 0

    return max_left_index, max_right_index, max_left + max_right




class TestSolution(unittest.TestCase):

    def test_middle(self):
        self.assertEqual(get_middle_subarray([2,-2,3,-5,8,-4,-2], 3), (2, 4, 6))
        self.assertEqual(get_middle_subarray([2,3,-5,8], 1), (0, 3, 8))
        self.assertEqual(get_middle_subarray([-2,-3,-5,-8], 1), (1, 2, -8))

    def test_case(self):
        examples = (
            (([13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7], 0, 16), (7, 10, 43)),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(maximum_subarray(*first), second,
                         msg="first: {}; second: {}".format(first, second))
        self.assertEqual(brute_force_maximum_subarray(*first), second,
                         msg="first: {}; second: {}".format(first, second))
        self.assertEqual(incr_maximum_subarray(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

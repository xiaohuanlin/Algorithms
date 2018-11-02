'''

Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:
Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.
Example 1:
Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
Example 2:
Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.

'''
import unittest


class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        import bisect
        min_list = []
        heaters = sorted(heaters)
        # calculate all min distance of house to heater
        for house in houses:
            insert = bisect.bisect(heaters, house)
            # avoid insert == 0
            min_dis = min(abs(house - heater) for heater in heaters[insert-(insert > 0):insert+1])

            min_list.append(min_dis)
        # return the max value to ensure all house have a heater
        return max(min_list)


class TestSolution(unittest.TestCase):

    def test_findRadius(self):
        examples = (
            (([1,2,3],[2]), 1),
            (([1,2,3,4],[1,4]), 1),
            (([1], [1,2,3,4]), 0),
            (([1,2,3,5,15], [2,30]), 5),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findRadius(*first), second, msg="first: {}; second: {}".format(first, second))

unittest.main()
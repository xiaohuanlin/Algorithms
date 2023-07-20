'''
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

Return a list of transactions that are possibly invalid. You may return the answer in any order.

 

Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]
 

Constraints:

transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000.
'''
from typing import *

import unittest


from collections import defaultdict
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = set()
        maps = defaultdict(list)
        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(',')
            for other_time, other_city, other_index in maps[name]:
                if city != other_city and abs(other_time - int(time)) <= 60:
                    res.add(i)
                    res.add(other_index)
            
            if int(amount) > 1000:
                res.add(i)
            maps[name].append((int(time), city, i))
        return [transactions[i] for i in res]


        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((["alice,20,800,mtv","bob,50,1200,mtv"],),["bob,50,1200,mtv"]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().invalidTransactions(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

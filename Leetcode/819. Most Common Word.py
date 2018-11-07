'''

Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.



Example:

Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.


Note:

1 <= paragraph.length <= 1000.
1 <= banned.length <= 100.
1 <= banned[i].length <= 10.
The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
There are no hyphens or hyphenated words.
Words only consist of letters, never apostrophes or other punctuation symbols.

'''
import unittest


class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        from collections import Counter
        count_dict = Counter()
        word_list = []
        for s in paragraph:
            if s in "!?',;. ":
                word = ''.join(word_list)
                if word:
                    count_dict[word.lower()] += 1
                word_list = []
            else:
                word_list.append(s)
        else:
            word = ''.join(word_list)
            if word:
                count_dict[word.lower()] += 1
        for ban in banned:
            count_dict[ban] = 0
        # print(count_dict)
        return count_dict.most_common(1)[0][0]



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (('Bob hit a ball, the hit BALL flew far after it was hit.', ["hit"]), 'ball'),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().mostCommonWord(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

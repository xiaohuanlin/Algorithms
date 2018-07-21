'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''

# class Solution:
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         stack = []
#         map_dict = {
#             '}': '{',
#             ')': '(',
#             ']': '['
#         }

#         s = list(s)

#         if len(s) == 1:
#             # it is not possible to have an individual
#             return False

#         while s:
#             n = s.pop(0)
#             if stack:
#                 if n in ('}', ')', ']'):
#                     if map_dict.get(n) != stack[-1]:
#                         return False
#                     else:
#                         # pop the value that have been matched
#                         stack.pop()
#                         return self.isValid(stack + s)
#                 else:
#                     # judge if there are all open brackets
#                     if len(s) == 0:
#                         return False
#                     stack.append(n)
#             else:
#                 stack.append(n)
#         return True


# class Solution:
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         s = list(s)
#         if len(s) == 0:
#             return True

#         for index in range(len(s)):
#             if s[index] in ('}', ')', ']'):
#                 break
#         else:
#             return False

#         map_dict = {
#             '}': '{',
#             ')': '(',
#             ']': '['
#         }

#         if index:
#             if map_dict.get(s[index]) == s[index-1]:
#                 s.pop(index)
#                 s.pop(index-1)
#                 return self.isValid(s)
#         return False
        

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [], 
        paren_map = {
            ')': '(', 
            ']': '[', 
            '}': '{'
            }
        for c in s:
            if c not in paren_map: 
                stack.append(c)
            elif not stack or paren_map[c] != stack.pop(): 
                return False
        return not stack


#Solution 1: Using split() method to split the string into words and then return the length of the last word.
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words=s.split()
        return len(words[-1])
    

#Solution 2: Using two pointers to traverse the string from the end and count the characters of the last word.
# class Solution(object):
#     def lengthOfLastWord(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         i = len(s) - 1
#         count = 0
#         while i >= 0 and s[i] == ' ':
#             i -= 1
#         while i >= 0 and s[i] != ' ':
#             count += 1
#             i -= 1     
#         return count
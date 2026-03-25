class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = list(len(word) for word in s.split())

        return words[-1]

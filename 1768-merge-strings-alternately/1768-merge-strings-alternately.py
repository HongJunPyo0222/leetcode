class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ""
        if len(word1) >= len(word2):
            longStr = word1
            shortStr = word2
        else:
            longStr = word2
            shortStr = word1
        index = 0
        for index in range(0, len(shortStr)):
            res += word1[index]
            res += word2[index]
        for index in range(index + 1, len(longStr) ):
            res += longStr[index]

        return res
        
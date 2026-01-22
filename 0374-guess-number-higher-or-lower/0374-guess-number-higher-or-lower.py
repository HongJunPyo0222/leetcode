# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        min = 1
        max = n
        n = (min + max)//2
        print(n)
        while True:
            print(n)
            if guess(n) == 0:
                return n
            if guess(n) == -1:
                max = n - 1
            if guess(n) == 1:
                min = n + 1
            n = (min + max)//2
            
        
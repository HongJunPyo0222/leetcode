class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        arrT = [0, 1, 1]
        for i in range(3, 38):
            arrT.append(arrT[i - 1] + arrT[i - 2] + arrT[i -3])

        return arrT[n]
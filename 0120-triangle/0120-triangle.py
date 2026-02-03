class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for index in range(1, len(triangle)):
            for i in range(len(triangle[index])):
                if i == 0:
                    triangle[index][0] += triangle[index -1][0]
                elif i == len(triangle[index]) - 1:
                    triangle[index][-1] += triangle[index - 1][-1]
                else:
                    triangle[index][i] += min(triangle[index-1][i - 1], triangle[index - 1][i])

        for element in triangle:
            print(element)

        return min(triangle[-1])
"""
2
3 4
6 5 7
4 1 8 3

"""
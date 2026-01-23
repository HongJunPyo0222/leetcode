class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        matrix = [[0 for _ in range(n)]for _ in range(m)]
        matrix[0] = [1 for _ in range(n)]
        for index in range(m):
            matrix[index][0] = 1

        for element in matrix:
            print(element) 
        
        for y in range(1, m):
            for x in range(1, n):
                matrix[y][x] = matrix[y - 1][x] + matrix[y][x -1]

        return matrix[m - 1][n-1]
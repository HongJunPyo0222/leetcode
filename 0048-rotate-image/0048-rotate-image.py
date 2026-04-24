class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        q = []
        lenk = len(matrix)
        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                q.append([val, x, y])
        maxlen = len(matrix) - 1
        print(q)
        half = len(matrix)/ 2
        while q:
            node = q.pop()
            print(node)
            val, x, y = node
            matrix[x][maxlen - y] = val

        for row in matrix:
            print(row)


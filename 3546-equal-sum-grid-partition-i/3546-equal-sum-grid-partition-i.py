class Solution(object):
    def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        
        sumA = 0
        for row in grid:
            sumA += sum(row)
        
        
        sumB = 0

        for row in grid:
            sumRow = sum(row)
            sumA -= sumRow
            sumB += sumRow
            if sumA == sumB:
                return True

        transposedGrid = list(zip(*grid))
        SumA = 0
        sumB = 0
        print(transposedGrid)
        for row in transposedGrid:
            sumA += sum(row)
        print(sumA)
        for row in transposedGrid:
            sumRow = sum(row)
            sumA -= sumRow
            sumB += sumRow
            print(sumA, sumB)
            if sumA == sumB:
                return True
        
        return False
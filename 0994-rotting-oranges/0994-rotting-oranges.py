import copy
class Solution(object):
    # 오렌지가 다 썩을때 까지 시간
    # 오렌지가 다 안썩는 다면 -1을 리턴
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]
    def inRange(self, grid, x, y):
        lnX = len(grid[0])
        lnY = len(grid)
        return x >=0 and x < lnX and y >=0 and y < lnY

    def checkRotten(self, grid, x, y):
        return self.inRange(grid, x, y) and grid[y][x] == 1

    def traversal_grid(self, grid, already_rotten):
        
        for y in range(len(already_rotten)):
            for x in range(len(grid[0])):
                if already_rotten[y][x] == 2:
                    #print("currentX:", x, "currentY: ", y)
                    for dx, dy in zip(self.dxs, self.dys):
                        nextX, nextY = x + dx, y + dy
                        #print("nextX:", nextX, "nextY: ", nextY)
                        if self.checkRotten(grid, nextX, nextY):
                            grid[nextY][nextX] = 2
                            #print("rottenated!!!")
        
        return grid
                
                

    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        already_rotten = copy.deepcopy(grid)
        count = 0
        while True:
            gridBefore = copy.deepcopy(grid)
            grid = self.traversal_grid(grid, already_rotten)
            count +=1
            if gridBefore == grid:
                break
            already_rotten = copy.deepcopy(grid)
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    return -1
        
        return count -1




        

        


from collections import deque

class Solution(object):

    def inRange(self,x, y, grid):
        return x>=0 and x < len(grid[0]) and y >=0 and y < len(grid)

    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool

            u
        l  d r
        """

        for row in grid:
            print(row)
        

        visited = [[0 for _ in grid[0]]for _ in grid]
        visited[0][0] = 1

        for row in visited:
            print(row)

        q = deque()
        x =0
        y = 0
        if grid[y][x] == 1:
            q.append([x + 1, y, "right"])
        elif grid[y][x] == 2:
            q.append([x, y+1, "down"])
        elif grid[y][x] == 3:
            q.append([x, y+1, "down"])
        elif grid[y][x] == 4:
            q.append([x+1, y,"right"])
            q.append([x, y+1,"down"])
        elif grid[y][x] == 5:
            q.append([x, y-1, "up"])        
            q.append([x - 1, y, "right"])
        elif grid[y][x] == 6:
            q.append([x+1, y, "right"])
            q.append([x, y - 1, "up"])
        
        count = 0

        while(q):
            
                
            x, y, toward= q.popleft()


            
            if not self.inRange(x, y, grid):
                continue
            
            if visited[y][x] == 1:
                continue

            

            

            if toward =="right":
                if grid[y][x] == 1:
                    visited[y][x] = 1
                    if self.inRange(x+1, y, grid):    
                       q.append([x+1, y, "right"])
                       


                if grid[y][x] == 3:
                    visited[y][x] = 1
                    if self.inRange(x, y, grid):    
                        q.append([x, y+1, "down"])

                if grid[y][x] == 5:
                    visited[y][x] = 1
                    if self.inRange(x, y,grid): 
                        q.append([x, y - 1, "up"])

            elif toward =="down":
                if grid[y][x] == 2:
                    visited[y][x] = 1

                    if self.inRange(x, y,grid): 
                        
                        q.append([x, y+ 1, "down"])

                if grid[y][x] == 5:
                    visited[y][x] = 1
                    if self.inRange(x, y,grid): 
                        q.append([x - 1, y, "left"])

                if grid[y][x] == 6:
                    visited[y][x] = 1
                    if self.inRange(x, y,grid): 
                        q.append([x + 1, y,"right"])
            elif toward =="up":
                if grid[y][x] == 2:
                    visited[y][x] = 1
                    if self.inRange(x, y,grid): 
                        q.append([x, y - 1, "up"])
                if grid[y][x] == 3:
                    visited[y][x] = 1
                    if self.inRange(x, y,grid): 
                        q.append([x-1, y, "left"])
                if grid[y][x] == 4:
                    visited[y][x] = 1
                    if self.inRange(x, y,grid): 
                        q.append([x + 1, y, "right"])
            elif toward == "left":
                if grid[y][x] == 1:
                    visited[y][x] = 1
                    if self.inRange(x, y,grid): 
                        q.append([x - 1, y, "left"])
                if grid[y][x] == 4:
                    visited[y][x] = 1
                    if self.inRange(x, y,grid): 
                        q.append([x, y + 1,"down"])
                if grid[y][x] == 6:
                    visited[y][x] = 1
                    if self.inRange(x, y,grid): 
                        q.append([x, y - 1,"up"])

                




        if visited[len(grid)-1][len(grid[0])-1] == 1:
            return True
        else:
            return False

        
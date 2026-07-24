from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        answer = 0
        dxs = [0, 1, 0, -1]
        dys = [1, 0, -1, 0]
        w = len(grid[0])
        h = len(grid)

        def in_range(nx, ny):
            return nx >=0 and nx < w and ny >= 0 and ny < h

        def can_move(nx, ny):
            return in_range(nx, ny) and checked[ny][nx] == False and grid[ny][nx] == '1'

        checked = [[False] * w for _ in range(h)]

        for row in grid:
            print(row)
        print()
        for row in checked:
            print(row)

        def spread(x, y):
            q = deque()
            q.append([x, y])
            checked[y][x] =True
            print(q)
            while(q):
                x, y = q.popleft()
                for dx, dy in zip(dxs, dys):
                    if can_move(x + dx, y + dy):
                        q.append([x + dx, y + dy])
                        checked[y + dy][x + dx] = True
                        print("spread")
            

        for y in range(h):
            for x in range(w):
                if checked[y][x] == True:
                    continue

                if grid[y][x] == '0':
                    continue
                print("x= ", x, "y = ",y)
                spread(x, y)
                answer +=1

                

                
        
        
        return answer
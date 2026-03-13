from collections import deque

class Solution(object):
    def in_range(self, maze, next_x, next_y):
        width = len(maze[0])
        height = len(maze)
        return next_x >= 0 and next_x < width and next_y >= 0 and next_y < height
    
    def can_move(self, maze, next_x, next_y):
        return self.in_range(maze, next_x, next_y) and maze[next_y][next_x] != '+'
    
    def is_goal(self, maze, next_x, next_y, entrance):
        width = len(maze[0])
        height = len(maze)

        return (next_x == 0 or next_x == width - 1 or next_y == 0 or next_y == height - 1) and ([next_y, next_x] != entrance)
        
    def nearestExit(self, maze, entrance):
        width = len(maze[0])
        height = len(maze)
        visited = [[False for _ in range(width)] for _ in range(height)]

        dxs = [0, 1, 0, -1]
        dys = [1, 0, -1, 0]

        q = deque()
        q.append([entrance, 0])
        

        visited[entrance[0]][entrance[1]] = True 

        while q:
            [now_y, now_x], count = q.popleft()
            
            for dx, dy in zip(dxs, dys):
                next_x = now_x + dx
                next_y = now_y + dy
                
                if self.can_move(maze, next_x, next_y) and visited[next_y][next_x] == False:
                    if self.is_goal(maze, next_x, next_y, entrance):
                        return count + 1
                    else:
                        q.append([[next_y, next_x], count + 1])

                        visited[next_y][next_x] = True 
                        
        return -1


maze = [
    ["+",".","+","+","+","+","+"],
    ["+",".","+",".",".",".","+"],
    ["+",".","+",".","+",".","+"],
    ["+",".",".",".","+",".","+"],
    ["+","+","+","+","+",".","+"]
]
entrance = [0,1]
k = Solution()

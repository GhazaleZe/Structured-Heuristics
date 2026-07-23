
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        green = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c]==1:
                    green +=1
        
        if green == 0:
            return 0

        time_count = 0
        while queue and green > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                    nr, nc = r+ dr, c+dc

                    if 0<= nr < rows and 0<= nc < cols and grid[nr][nc] ==1:
                        grid[nr][nc] = 2
                        green -= 1

                        queue.append((nr, nc))
            time_count +=1
        if green ==0:
            return time_count 
        else:
            return -1
                
                    


        
from collections import deque
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        l, r = 0, n*n-1
        while l+1 < r :
            mid = (l+r)//2
            if self.bfs(grid, mid, n) :
                r = mid
            else :
                l = mid
        if self.bfs(grid, l, n) :
            return l
        else :
            return r
    
    def bfs(self, grid, t, n) :
        queue = deque([(0, 0)])
        visited = set((0, 0))
        while queue :
            x, y = queue.popleft()
            if grid[x][y] <= t :
                if x == y == n-1 :
                    return True
                for i, j in [(0, 1), (0, -1), (-1, 0), (1, 0)] :
                    if 0 <= x+i < n and 0 <= y+j < n and (x+i, y+j) not in visited :
                        visited.add((x+i, y+j))
                        queue.append((x+i, y+j))
        return False
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid :
            return 0
        if grid[0][0] != 0 :
            return -1
        queue = deque([(0, 0)])
        res = 0
        n = len(grid)
        visited = set((0, 0))
        while queue :
            res += 1
            for i in range(len(queue)) :
                x, y= queue.popleft()
                if x == y == n-1 :
                    return res
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)] :
                    if 0 <= x+dx < n and 0 <= y+dy < n and (x+dx, y+dy) not in visited and grid[x+dx][y+dy] == 0 :
                        queue.append((x+dx, y+dy))
                        visited.add((x+dx, y+dy))
        return -1
from collections import deque
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix :
            return []
        m = len(matrix)
        n = len(matrix[0])
        pacific = [(0, i) for i in range(n)] + [(j, 0) for j in range(1, m)]
        atlantic = [(m-1, i) for i in range(n)] + [(j, n-1) for j in range(0, m-1)]
        palist = self.bfs(matrix, pacific, m, n)
        atlist = self.bfs(matrix, atlantic, m, n)
        return list(set(palist)&set(atlist))
    
    def bfs(self, matrix, reachable, m, n) :
        queue = deque(reachable)
        while queue :
            x, y = queue.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)] :
                if 0 <= x+dx < m and 0 <= y+dy < n and (x+dx, y+dy) not in reachable \
                and matrix[x][y] <= matrix[x+dx][y+dy] :
                    queue.append(((x+dx, y+dy)))
                    reachable.append((x+dx, y+dy))
        return reachable
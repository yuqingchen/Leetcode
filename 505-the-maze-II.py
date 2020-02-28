from heapq import heappop, heappush, heapify
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        heap = [(0, start[0], start[1])]
        heapify(heap)
        dists = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        visited = {(start[0], start[1]) : 0}
        while heap :
            #print(heap)
            dis, x, y = heappop(heap)
            if [x, y] == destination :
                return dis
            for dx, dy in dists :
                level = 0
                nx = x
                ny = y
                while 0 <= nx + dx < len(maze) and 0 <= ny + dy < len(maze[0]) and maze[nx + dx][ny + dy] != 1 :
                    nx += dx
                    ny += dy
                    level += 1
                if (nx , ny ) not in visited or dis + level < visited[(nx, ny)] :
                    visited[(nx, ny)] = dis + level
                    heappush(heap, (dis + level, nx, ny))
        return -1
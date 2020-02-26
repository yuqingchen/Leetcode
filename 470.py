from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        queue = deque([start])
        dist = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue :
            x, y = queue.popleft()
            maze[x][y] = 2
            if [x, y] == destination :
                return True
            for dx, dy in dist :
                nx = x + dx
                ny = y + dy
                while 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != 1 :
                    nx += dx
                    ny += dy
                nx -= dx
                ny -= dy
                if maze[nx][ny] == 0 :
                    queue.append([nx, ny])
        return False
           
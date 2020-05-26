from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        if not board :
            return -1
        res = 0
        n = len(board)
        visited = set()
        visited.add(1)
        queue = deque([1])
        while queue :
            for _ in range(len(queue)) :
                node = queue.popleft()
                if node == n*n :
                    return res
                for d in [1, 2, 3, 4, 5, 6] :
                    if node+d <= n*n and node+d not in visited :
                        visited.add(node+d)
                        x = n - ((node+d -1)//n) -1
                        if ((node+d -1)//n)%2 == 1 :
                            y = n  - ((node+d -1)%n) -1
                        else :
                            y = (node + d -1) % n
                        if board[x][y] == -1 :
                            newnode = node + d
                        else :
                            newnode = board[x][y]
                        queue.append(newnode)
            res += 1
        return -1
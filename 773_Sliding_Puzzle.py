from collections import deque
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = {0:[1, 3], 1:[0, 2, 4], 2:[1, 5], 3:[0, 4], 4:[1, 3, 5], 5:[2, 4]}
        visited = set()
        res = 0
        s = "".join(str(c) for row in board for c in row)
        queue = deque([(s, s.index('0'))])
        visited.add(s)
        while queue :
            for _ in range(len(queue)) :
                node, index = queue.popleft()
                if node == '123450' :
                    return res
                arr = [c for c in node]
                for move in moves[index] :
                    newarr = arr[:]
                    newarr[index], newarr[move] = newarr[move], newarr[index]
                    newnode = "".join(newarr)
                    if newnode not in visited :
                        queue.append((newnode, move))
                        visited.add(newnode)
            res += 1
        return -1
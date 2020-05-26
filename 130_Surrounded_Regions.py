from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue = deque([])
        for i in range(len(board)) :
            for j in range(len(board[0])) :
                if (i in [0, len(board) - 1] or j in [0, len(board[0]) - 1]) and board[i][j] == 'O' :
                    queue.append((i, j))
        while queue :
            x, y = queue.popleft()
            if 0<=x<len(board) and 0<=y<len(board[0]) and board[x][y] == "O":
                board[x][y] = "V"
                queue.append((x-1, y))
                queue.append((x+1, y))
                queue.append((x, y-1))
                queue.append((x, y+1))
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == "O":
                    board[x][y] = "X"
                elif board[x][y] == "V":
                    board[x][y] = "O"
        return 
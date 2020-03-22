class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0 :
            return False
        n, m = len(matrix), len(matrix[0])
        i, j = n - 1, 0 
        while i >= 0 and j < m :
            if matrix[i][j] == target :
                return True 
                i -= 1  
            elif matrix[i][j] > target :
                i -= 1 
            elif matrix[i][j] < target :
                j += 1 
        return False
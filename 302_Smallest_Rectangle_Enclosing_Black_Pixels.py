class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        if len(image) == 0 or len(image[0]) == 0 :
            return 0 
        left, right, up, down = 0, 0, 0, 0
        
        start, end = 0, y
        while start + 1 < end :
            mid = (start + end) //2
            if self.CheckCol(image, mid) :
                end = mid 
            else :
                start = mid 
        if self.CheckCol(image, start) :
            left = start
        else :
            left = end 
            
        start, end = y, len(image[0]) - 1 
        while start + 1 < end :
            mid = (start + end) // 2 
            if self.CheckCol(image, mid) :
                start = mid 
            else :
                end = mid 
        if self.CheckCol(image, end) :
            right = end 
        else:
            right = start
            
        start, end = 0, x
        while start + 1 < end :
            mid = (start + end) // 2 
            if self.CheckRow(image, mid) :
                end = mid 
            else :
                start = mid 
        if self.CheckRow(image, start) :
            up = start
        else :
            up = end 
            
        start, end = x, len(image) - 1 
        while start + 1 < end :
            mid = (start + end) // 2 
            if self.CheckRow(image, mid) :
                start = mid 
            else :
                end = mid 
        if self.CheckRow(image, end) :
            down = end
        else :
            down = start
            
        return (down - up + 1) * (right - left + 1)
        
    def CheckCol(self, image, col) :
        for i in range(len(image)) :
            if image[i][col] == '1' :
                return True
        return False
    
    def CheckRow(self, image, row) :
        for i in range(len(image[0])) :
            if image[row][i] == '1' :
                return True
        return False
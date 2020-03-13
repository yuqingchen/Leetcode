class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        firstElement = reader.get(0)
        if firstElement == target :
            return 0
        if firstElement > target :
            return -1 
        start, end = 0, 1
        while reader.get(end) <= target :
            end <<= 1 
        while start + 1 < end :
            mid = (start + end) // 2 
            if reader.get(mid) < target :
                start = mid 
            else :
                end = mid 
        if reader.get(start) == target :
            return start
        if reader.get(end) == target :
            return end 
        return -1
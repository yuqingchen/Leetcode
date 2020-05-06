class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        mindiff = sys.maxsize
        
        def timediff(time1, time2) :
            t1h, t1m = time1.split(':')
            t2h, t2m = time2.split(':')
            diff = (int(t2h) - int(t1h)) * 60
            diff += int(t2m) - int(t1m)
            return diff
        
        for i in range(1, len(timePoints)) :
            time2, time1 = timePoints[i], timePoints[i -1]
            mindiff = min(timediff(time1, time2), mindiff)
        
        last = timediff(timePoints[-1], timePoints[0]) + 24 * 60
        return min(mindiff, last)
from collections import deque
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flight = defaultdict(list)
        for [start, end] in tickets :
                flight[start].append(end)
        res = ['JFK']
        def dfs(start) :
            if len(res) == len(tickets) + 1 :
                return res
            candi = sorted(flight[start])
            for c in candi :
                flight[start].remove(c)
                res.append(c)
                worked = dfs(c)
                if worked :
                    return worked
                res.pop()
                flight[start].append(c)
        return dfs('JFK')
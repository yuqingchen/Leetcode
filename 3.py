class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = length = 0
        visited = {}
        for i in range(len(s)) :
            #some character in visited may occur after start
            if s[i] in visited and start <= visited[s[i]]:
                start = visited[s[i]] + 1 
            else :
                length = max(length, i - start + 1)
            visited[s[i]] = i
        return length
        
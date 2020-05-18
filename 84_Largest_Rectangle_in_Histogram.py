class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        n = len(heights)
        res = 0
        for i in range(n) :
            while heights[i] < heights[stack[-1]] :
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h*w)
            stack.append(i)
        return res
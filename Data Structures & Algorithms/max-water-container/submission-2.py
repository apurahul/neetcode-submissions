class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxarea = 0


        for i in range(len(heights) - 1):
            for j in range(i + 1, len(heights)):
                h = min(heights[i], heights[j])
                b = j - i

                area = h * b

                maxarea = max(area,maxarea)
        
        return maxarea
                
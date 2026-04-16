class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_height = 0


        l, r = 0, len(heights) -1

        while l < r:
            breadth = r - l 

            if heights[l] == heights[r]:
                height = heights[l]
                l += 1
                r -= 1

            elif heights[l] < heights[r]:
                height = heights[l]
                l += 1
            else:
                height = heights[r]
                r -= 1
            size = breadth * height
            
            max_height = max(max_height, size)

        return max_height    
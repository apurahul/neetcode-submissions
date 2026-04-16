class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxarea = 0


        # for i in range(len(heights) - 1):
                #     for j in range(i + 1, len(heights)):
                        #         h = min(heights[i], heights[j])
                                #         b = j - i

                                        #         area = h * b

                                                #         maxarea = max(area,maxarea)
                                                        
                                                                # return

                


        l, r = 0, len(heights) - 1

        while l < r:
                breadth = r - l
                if heights[l] <= heights[r]:
                    length = heights[l]
                    l += 1
                else:
                    length = heights[r]
                    r -= 1
                
                area = length * breadth
                maxarea = max(maxarea, area)
        return maxarea
        
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxa = 0

        p1 = 0
        p2 = len(heights) - 1

        while p1 < p2:
            if heights[p1] < heights[p2]:
                minh = heights[p1]
            else:
                minh = heights[p2]
            
            if ((p2-p1) * minh) > maxa:
                maxa = ((p2-p1) * minh)

            if heights[p1] < heights[p2]:
                p1+=1
            else:
                p2-=1
        
        return maxa
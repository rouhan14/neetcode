class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxa = 0

        left, right = 0, len(heights)-1

        while left < right:
            min_h=0
            if heights[left] < heights[right]:
                min_h = heights[left]
            else:
                min_h = heights[right]
            
            vol = min_h * (right-left)

            if vol > maxa:
                maxa = vol
            
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        
        return maxa
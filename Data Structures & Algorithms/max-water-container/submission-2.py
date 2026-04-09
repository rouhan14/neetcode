class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxa = 0

        left = 0
        right = len(heights)-1

        while left < right:

            min_h = min(heights[left], heights[right])
            vol = min_h * (right - left)

            maxa = max(maxa, vol)

            if heights[left] == min_h:
                left+=1
                continue
            else:
                right-=1
        
        return maxa


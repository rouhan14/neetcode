class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water=0

        i, j = 0, len(heights)-1

        while i < j:
            temp = min(heights[i], heights[j])

            if water < (temp*(j-i)):
                water = temp*(j-i)
            
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1

        return water
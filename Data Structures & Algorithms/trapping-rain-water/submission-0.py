class Solution:
    def trap(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) - 1

        maxw = 0
        left_max, right_max = 0, 0
        while p1 < p2:
            if height[p1] < height[p2]:
                if height[p1] >= left_max:
                    left_max = height[p1]
                else:
                    maxw += left_max - height[p1]
                p1+=1
            else:
                if height[p2] >= right_max:
                    right_max = height[p2]
                else:
                    maxw += right_max - height[p2]
                p2-=1

        return maxw


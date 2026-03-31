class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_to = {}

        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in num_to:
                return [num_to[temp], i]
            
            num_to[nums[i]] = i

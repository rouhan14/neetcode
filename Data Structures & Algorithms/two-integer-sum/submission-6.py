class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums)-1

        myHashMap = dict()

        for i in range(len(nums)):
            if target - nums[i] in myHashMap:
                return [myHashMap[target - nums[i]], i]
            else:
                myHashMap[nums[i]] = i


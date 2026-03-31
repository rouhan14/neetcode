class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sett = {}
        for i in range(len(numbers)):
            temp = target - numbers[i]
            if temp in sett:
                return [sett[temp]+1, i+1]
            
            sett[numbers[i]] = i

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-i for i in nums]
        heapq.heapify(heap)

        count = 0
        while count < k:
            temp = -heapq.heappop(heap)
            count+=1

        return temp
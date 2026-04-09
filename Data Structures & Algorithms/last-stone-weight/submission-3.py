class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) ==1:
            return stones[0]
        
        heap = [-i for i in stones]
        heapq.heapify(heap)

        first = 0
        second = 0
        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            temp = abs(first-second)
            heapq.heappush(heap, -temp)
        return -heap[0]
        

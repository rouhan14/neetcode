class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) ==1:
            return stones[0]
        first=0
        second=0
        heap = [-i for i in stones]
        heapq.heapify(heap)
        while heap:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            temp = first - second
            heapq.heappush(heap, temp)

            if len(heap) == 1:
                return -heapq.heappop(heap)
        

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = dict()
        heap = []

        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        
        for num, freq in hashMap.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []

        while heap:
            freq, num = heapq.heappop(heap)
            result.append(num)
        
        return result
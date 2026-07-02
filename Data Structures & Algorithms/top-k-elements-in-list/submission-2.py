class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        heap = []
        res = []

        for c in count:
            heapq.heappush(heap, (count[c], c))
            if len(heap) > k:
                heapq.heappop(heap)
            
        for i in range(k):
            res.append(heapq.heappop(heap)[1]);

        return res

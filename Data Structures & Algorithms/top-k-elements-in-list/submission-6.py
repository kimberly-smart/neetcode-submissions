class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        heap = []
        for c in count:
            heapq.heappush(heap, (count[c], c))
            if len(heap) > k:
                heapq.heappop(heap)
            
        res = []
        for h in heap:
            res.append(h[1])
        
        return res
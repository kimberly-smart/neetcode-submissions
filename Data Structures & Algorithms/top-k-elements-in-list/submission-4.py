class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [1,2,2,3,3,3]
        count = {}
        for num in nums: 
            count[num] = 1 + count.get(num, 0)
        
        #1=1, 2=2, 3=3
        heap = []

        for c in count:
            heapq.heappush(heap, (count[c], c))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []

        for h in heap:
            res.append(h[1])
        
        return res
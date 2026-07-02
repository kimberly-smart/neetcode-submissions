class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-s for s in stones]
        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            fheap = - heapq.heappop(maxheap)
            sheap = - heapq.heappop(maxheap) if maxheap else 0

            sub = fheap - sheap
            heapq.heappush(maxheap, -sub)
        
        return -heapq.heappop(maxheap)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for n in stones:
            heapq.heappush(heap, -n)

        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap) if heap else 0

            sub = first - second
            heapq.heappush(heap, -sub)
        
        return -heapq.heappop(heap)

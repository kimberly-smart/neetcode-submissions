class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones) if stones else 0

            sub = first - second
            heapq.heappush(stones, -sub)
        
        return -heapq.heappop(stones)

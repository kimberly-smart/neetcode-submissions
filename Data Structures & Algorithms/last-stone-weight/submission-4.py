class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-n for n in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            firststone = -heapq.heappop(stones)
            secondstone = -heapq.heappop(stones) if stones else None

            smashval = firststone - secondstone
            heapq.heappush(stones, -smashval)
        
        return -heapq.heappop(stones)

        
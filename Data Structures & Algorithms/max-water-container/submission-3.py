class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        mostcontain = 0

        while i<j:
            between = j-i
            minval = min(heights[i], heights[j])
            mostcontain = max(mostcontain, minval * between)

            if heights[i] < heights[j]:
                i += 1
            else:
                j-=1
        return mostcontain

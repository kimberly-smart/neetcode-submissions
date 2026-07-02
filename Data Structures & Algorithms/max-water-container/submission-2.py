class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxval = 0
        i=0
        j=len(heights)-1

        while i<j:
            smaller = min(heights[i], heights[j])
            space = j-i
            watercontain = smaller * space

            maxval = max(maxval, watercontain)

            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1
        return maxval
        
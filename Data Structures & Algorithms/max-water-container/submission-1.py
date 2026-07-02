class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        pt1 = 0
        pt2 = len(heights)-1

        while pt1 < pt2:
            between = pt2-pt1
            smallval = min(heights[pt1], heights[pt2])
            res = max(res, smallval*between)

            if heights[pt1] > heights[pt2]:
                pt2 -= 1
            else:
                pt1 += 1
        return res
        
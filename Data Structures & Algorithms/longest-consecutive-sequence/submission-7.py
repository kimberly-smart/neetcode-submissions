class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0

        for n in nums:
            if n-1 not in numset:
                seq = 0
                while n in numset:
                    n += 1
                    seq += 1
                res = max(res, seq)
        return res
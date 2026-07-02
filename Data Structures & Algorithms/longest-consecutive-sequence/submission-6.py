class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        for n in nums:
            if n-1 not in numset:
                seq = 0
                while n in numset:
                    seq += 1
                    n += 1
                res = max(res, seq)
        
        return res
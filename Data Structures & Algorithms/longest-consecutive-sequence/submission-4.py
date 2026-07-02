class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setval = set(nums)
        longest = 0

        for n in setval:
            if(n-1) not in setval:
                len = 1
                while(n+1) in setval:
                    len+=1
                    n += 1
                longest = max(longest, len)
        return longest
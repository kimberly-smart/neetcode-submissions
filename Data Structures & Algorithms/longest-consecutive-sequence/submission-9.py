class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setval = set(nums)

        finalres = 0

        for n in nums:
            res = 0
            if n-1 not in setval:
                smallest = n
                res +=1

                while smallest+1 in setval:
                    res +=1
                    smallest +=1
            finalres = max(finalres, res)
        
        return finalres
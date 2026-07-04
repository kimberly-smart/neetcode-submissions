class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        setval = set()

        for r in range(len(s)):
            while s[r] in setval:
                setval.remove(s[l])
                l+=1
            
            res = max(res, r-l+1)
            setval.add(s[r])
        
        return res
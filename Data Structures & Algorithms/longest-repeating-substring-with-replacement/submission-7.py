class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashval = {}
        res = 0
        l=0

        for r in range(len(s)):
            hashval[s[r]] = 1 + hashval.get(s[r], 0)
            maxcontain = max(hashval.values())

            while (r-l+1) - maxcontain > k:
                hashval[s[l]] -= 1
                l+=1
            res = max(res, r-l+1)
        return res
                
            

            
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charcount = {}
        l = 0
        res = 0

        for r in range(len(s)):
            charcount[s[r]] = 1 + charcount.get(s[r], 0)

            while (r-l+1) - max(charcount.values()) > k:
                charcount[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        
        return res
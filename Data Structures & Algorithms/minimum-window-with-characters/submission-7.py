class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        count = {}
        for c in t:
            count[c] = 1 + count.get(c, 0)
        
        have = 0
        need = len(count)
        res = [-1,-1]
        reslen = float("inf")
        scount = {}
        l = 0

        for r in range(len(s)):
            c = s[r]
            scount[c] = 1 + scount.get(c, 0)

            if c in count and scount[c] == count[c]:
                have += 1
            
            while have == need:
                if r-l+1 < reslen:
                    res = [l, r]
                    reslen = r-l+1
                
                scount[s[l]] -= 1
                if s[l] in count and scount[s[l]] < count[s[l]]:
                    have -= 1
                
                l+=1
        
        l,r = res
        return s[l:r+1] if reslen != float("inf") else ""
                



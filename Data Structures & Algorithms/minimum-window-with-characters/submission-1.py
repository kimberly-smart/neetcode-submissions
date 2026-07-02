class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" : return ""
        tct, sct = {}, {}
        l = 0
        res,reslen = [-1,-1], float("infinity")

        for tchar in t:
            tct[tchar] = 1 + tct.get(tchar,0)
        
        need = len(tct)
        have = 0
        
        for r in range(len(s)):
            c = s[r]
            sct[c] = 1 + sct.get(c, 0)

            if c in tct and tct[c] == sct[c]:
                have +=1
            while have == need:
                if (r-l+1) < reslen:
                    res = [l, r]
                    reslen = r-l+1
                sct[s[l]] -= 1
                if s[l] in tct and sct[s[l]] < tct[s[l]]:
                    have -= 1
                l += 1
        
        l,r = res
        return s[l: r+1] if reslen != float("infinity") else ""
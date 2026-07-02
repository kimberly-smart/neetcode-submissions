class Solution:
# hello world
# [hello, world]
# 5#hello5#world
    def encode(self, strs: List[str]) -> str:
        encodeval = ""
        for st in strs:
            tempencode = str(len(st))+"#"+st
            encodeval += tempencode
        
        return encodeval

    def decode(self, s: str) -> List[str]:
        i=0
        res = []
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            slen = int(s[i:j])
            res.append(s[j+1:j+slen+1])
            i = j+slen+1
        return res

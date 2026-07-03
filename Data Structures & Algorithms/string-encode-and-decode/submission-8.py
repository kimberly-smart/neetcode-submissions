class Solution:

# 5#hello5#world
    def encode(self, strs: List[str]) -> str:
        decoder = ""

        for s in strs:
            decoder += str(len(s))+"#"+s
        
        return decoder

    def decode(self, s: str) -> List[str]:
# 5#hello5#world

        res = []
        i=0

        while i<len(s):
            j=i
            while s[j] != "#":
                j += 1
            
            num = int(s[i:j])
            res.append(s[j+1: j+num+1])
            i = j+num+1
        return res
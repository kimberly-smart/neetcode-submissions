class Solution:
    # Hello world
    # 5#Hello5#world
    def encode(self, strs: List[str]) -> str:
        encodestr = ""
        for st in strs:
            encodestr += str(len(st))+"#"+st

        return encodestr

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j=i
            while s[j] != "#":
                j += 1
            slen = int(s[i:j])
            res.append(s[j+1: j+slen+1])
            i=j+slen+1
        return res


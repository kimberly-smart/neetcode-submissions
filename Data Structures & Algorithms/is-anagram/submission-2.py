class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shashmap = {}
        thashmap = {}

        for c in s:
            if c in shashmap:
                shashmap[c] = shashmap.get(c,0) + 1
            else:
                shashmap[c] = 1
        for c in t:
            if c in thashmap:
                thashmap[c] = thashmap.get(c,0) +1
            else:
                thashmap[c] = 1
        
        return shashmap == thashmap


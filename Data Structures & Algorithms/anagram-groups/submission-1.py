class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        for st in strs:
            countChar = [0]*26

            for c in st:
                countChar[ord(c)-ord('a')] +=1

            res[tuple(countChar)].append(st)

        return list(res.values())     

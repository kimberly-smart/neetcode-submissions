class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        orderedList = []
        orderedDic = dict()
        for st in strs:
            orderedStr = ''.join(sorted(st))
            if orderedStr in orderedDic:
                orderedDic[orderedStr].append(st)
            else:
                orderedDic[orderedStr] = [st]
        orderedList = orderedDic.values()


        return list(orderedList)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]


        for st in strs:
            count = [0]*26
            for c in st:
                count[ord(c) - ord('a')] +=1
                # act
                # [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
            
            dic[tuple(count)].append(st)
        
        return list(dic.values())



        
            
            

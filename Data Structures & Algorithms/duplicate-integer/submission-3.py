class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ele = set()
        for n in nums:
            if n in ele:
                return True
            ele.add(n)
        
        return False
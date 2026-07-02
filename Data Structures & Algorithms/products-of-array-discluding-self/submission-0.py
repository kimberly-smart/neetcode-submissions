class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i, num in enumerate(nums):
            sum = 1;
            for j, num in enumerate(nums):
                if j != i:
                    sum = sum * nums[j]
            res.append(sum)
        
        return res
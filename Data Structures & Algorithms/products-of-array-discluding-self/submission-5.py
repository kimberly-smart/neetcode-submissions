class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre = 1

        for n in nums:
            res.append(pre)
            pre = n*pre
        
        post = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * post
            post = post*nums[i]
        
        return res


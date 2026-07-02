class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i,a in enumerate(nums):
            if i>0 and nums[i-1] == a:
                continue
            
            start = i+1
            end = len(nums) - 1
            
            while start < end:
                sum = a+nums[start]+nums[end]

                if sum > 0:
                    end -= 1
                elif sum < 0:
                    start += 1
                else:
                    res.append([a, nums[start], nums[end]])
                    end -=1
                    start += 1
                    while start < end and nums[start-1] == nums[start]:
                        start += 1
        return res
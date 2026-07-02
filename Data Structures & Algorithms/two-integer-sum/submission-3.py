class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numhash = {}
        res = []

        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in numhash:
                return [numhash[temp], i]
            
            numhash[nums[i]] = i
        
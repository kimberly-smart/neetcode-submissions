class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        hashmap = {}

        for i, num in enumerate(nums):
            sub = target - num

            if sub in hashmap:
                res.append(hashmap.get(sub))
                res.append(i)
            else:
                hashmap[num] = i

        return res; 
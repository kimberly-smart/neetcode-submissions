class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        hashmap = dict()
        for i,num in enumerate(nums):
            subtract = target - num

            if subtract in hashmap:
                result.append(hashmap.get(subtract))
                result.append(i)
            else:
                hashmap[num] = i
        return result

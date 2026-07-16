class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            num = nums[i]
            rem = target - num
            if rem in hashmap:
                return [hashmap[rem],i]
            hashmap[num] = i
        

        
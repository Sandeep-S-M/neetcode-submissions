class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i,num in enumerate(nums):
            rem = target - num
            if rem in prev:
                return [prev[rem],i]
            if num not in prev:
                prev[num] = i
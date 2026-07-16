class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()
        l,h = 0,len(nums)
        while l < h:
            m  = (l+h)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l += 1 
            else:
                h -= 1
        return -1

        
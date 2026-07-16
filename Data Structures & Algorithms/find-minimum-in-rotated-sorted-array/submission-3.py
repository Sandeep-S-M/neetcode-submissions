class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        min_ele = nums[r]
        while l < r:
            m = (l+r)//2
            if nums[m] < min_ele:
                min_ele = nums[m]
                r = m
            else:
                l += 1
        return min_ele
        
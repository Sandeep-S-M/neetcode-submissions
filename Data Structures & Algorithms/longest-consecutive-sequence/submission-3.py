class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        length = 1
        cnt = 1
        for i in range(1,len(nums)):
            val = nums[i-1]+1
            if nums[i] == val:
                cnt += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                cnt = 1
            length = max(length,cnt)
        return length




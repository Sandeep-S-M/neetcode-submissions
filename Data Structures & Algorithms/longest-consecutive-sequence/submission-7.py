class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        
        for num in nums:
            if num -1 not in nums_set:
                curr = num
                curr_len = 1
                while curr + 1 in nums_set:
                    curr += 1
                    curr_len += 1
                max_len = max(max_len,curr_len)
                if max_len > len(nums_set):
                    return max_len

        return max_len


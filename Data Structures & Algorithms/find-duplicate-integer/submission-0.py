class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        freq = [0]*(n+1)
        for n in nums:
            if freq[n]==0:
                freq[n] = 1
            else:
                return n


        
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prev = {}
        for i,num in enumerate(numbers):
            rem = target - num
            if rem in prev:
                return [prev[rem],i+1]
            prev[num] = i+1
        


            
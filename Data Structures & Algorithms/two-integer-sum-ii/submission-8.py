class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prev = {}
        for i in range(len(numbers)):
            rem = target - numbers[i]
            if rem in prev:
                return [prev[rem]+1,i+1]
            prev[numbers[i]] = i
        return []
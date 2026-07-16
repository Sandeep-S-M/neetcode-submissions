class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n= len(temperatures)
        result = [0]*n
        for i in range(n):
            for j in range(i+1,n):
                if temperatures[i] < temperatures[j]:
                    result[i] = j - i 
                    break
                else:
                    continue
        return result






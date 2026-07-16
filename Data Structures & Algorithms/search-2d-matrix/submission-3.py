class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0,len(matrix)
        while l < r:
            m = (l+r)//2
            matrix[m].sort()
            if target in matrix[m]:
                return True
            elif matrix[m][-1] < target: 
                l += 1
            else:
                r -= 1 
        return False





            
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = len(matrix)
        i = 0 
        while i < left:
            matrix[i].sort()
            if matrix[i][-1] > target:
                for mat in matrix[i][::-1]:
                    if mat == target:
                        return True
            elif matrix[i][-1] == target:
                return True
            i += 1;
        return False

                



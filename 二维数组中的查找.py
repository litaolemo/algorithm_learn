from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        lines = len(matrix)
        if lines == 0: return False
        col_max = len(matrix[0])
        col = 0
        if target < matrix[0][0]:return False
        if target > matrix[lines-1][col_max-1]:return False
        for line in range(lines):
            while col < col_max:
                num = matrix[line][col]
                if target == num:
                    return True
                col += 1
                if target < num:
                    if line == 0:
                        col -= 2
                        break
            else:
                col = 0
        return False



test = Solution()
print(test.findNumberIn2DArray(
    [[3, 3, 8, 13, 13, 18], [4, 5, 11, 13, 18, 20], [9, 9, 14, 15, 23, 23], [13, 18, 22, 22, 25, 27],
     [18, 22, 23, 28, 30, 33], [21, 25, 28, 30, 35, 35], [24, 25, 33, 36, 37, 40]],
21
))
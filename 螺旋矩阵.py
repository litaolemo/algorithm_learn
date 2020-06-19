from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:return []
        l, r, t, b = 0, len(matrix[0])-1, 0, len(matrix)-1
        num_count = (r+1) * (b+1)
        res_list = []
        count = 0
        while count <= num_count:
            for i in range(l,r+1):
                res_list.append(matrix[t][i])
                count += 1
            t += 1
            if count == num_count:return res_list
            for i in range(t,b+1):
                res_list.append(matrix[i][r])
                count += 1
            r -= 1
            if count == num_count: return res_list
            for i in range(r,l-1,-1):
                res_list.append(matrix[b][i])
                count += 1
            b -= 1
            if count == num_count: return res_list
            for i in range(b,t-1,-1):
                res_list.append(matrix[i][l])
                count += 1
            l += 1
            if count == num_count: return res_list
        return res_list

test = Solution()
print(test.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]))

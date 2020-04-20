# -*- coding:utf-8 -*-
# @Time : 2020/4/20 19:33
# @Author : litao


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        len_list = len(grid[0])
        extend_row = ["0" for x in range(len_list +1)]
        grid.append(extend_row)
        #print(grid)
        for row,row_data in enumerate(grid):
            if row == len_list:break
            row_data.append("0")
            print(grid)
            for line,line_data in enumerate(row_data):

                if line_data == "1":
                    if row_data[line-1] == "1" or grid[row-1][line] == "1":
                        pass
                    elif row_data[line+1] == "1":
                        pass
                    else:
                        print(line, line_data,row_data[line-1],grid[row-1][line])
                        count += 1
            print(count)
        return count

a = [["1","1","1"],["0","1","0"],["1","1","1"]]
b = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
c = [["1"]]
test = Solution()
print(test.numIslands(
a
))
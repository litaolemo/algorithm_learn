# -*- coding:utf-8 -*-
# @Time : 2020/4/20 19:33
# @Author : litao


class Solution(object):

    def dfs(self, grid, r, c):
        grid[r][c] = 0
        nr, nc = len(grid), len(grid[0])
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                self.dfs(grid, x, y)

    def numIslands(self, grid):
        """
            :type grid: List[List[str]]
            :rtype: int
            """
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    self.dfs(grid, r, c)

        # 深度优先
        return num_islands


# https://leetcode-cn.com/problems/number-of-islands/solution/dao-yu-shu-liang-by-leetcode/
a = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
b = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
c = [["1"]]
test = Solution()
print(test.numIslands(
    a
))

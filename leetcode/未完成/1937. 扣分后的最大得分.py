# -*- coding:utf-8 -*-
# @author :litao
# @Time :2021/7/20 11:53


"""
给你一个 m x n 的整数矩阵 points （下标从 0 开始）。一开始你的得分为 0 ，你想最大化从矩阵中得到的分数。

你的得分方式为：每一行 中选取一个格子，选中坐标为 (r, c) 的格子会给你的总得分 增加 points[r][c] 。

然而，相邻行之间被选中的格子如果隔得太远，你会失去一些得分。对于相邻行 r 和 r + 1 （其中 0 <= r < m - 1），选中坐标为 (r, c1) 和 (r + 1, c2) 的格子，你的总得分 减少 abs(c1 - c2) 。

请你返回你能得到的 最大 得分。

abs(x) 定义为：

如果 x >= 0 ，那么值为 x 。
如果 x < 0 ，那么值为 -x 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-number-of-points-with-cost
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        f = [0] * n
        for i in range(m):
            g = [0] * n
            best = float("-inf")
            # 正序遍历
            for j in range(n):
                best = max(best, f[j] + j)
                g[j] = max(g[j], best + points[i][j] - j)

            best = float("-inf")
            # 倒序遍历
            for j in range(n - 1, -1, -1):
                best = max(best, f[j] - j)
                g[j] = max(g[j], best + points[i][j] + j)

            f = g

        return max(f)



if __name__ == "__main__":
    test = Solution()
    print(test.maxPoints([[1,2,3],[1,5,1],[3,1,1]]))
# -*- coding:utf-8 -*-
# @author :litao
# @Time :2021/7/20 10:54

"""
1936. 新增的最少台阶数
给你一个 严格递增 的整数数组 rungs ，用于表示梯子上每一台阶的 高度 。当前你正站在高度为 0 的地板上，并打算爬到最后一个台阶。

另给你一个整数 dist 。每次移动中，你可以到达下一个距离你当前位置（地板或台阶）不超过 dist 高度的台阶。当然，你也可以在任何正 整数 高度处插入尚不存在的新台阶。

返回爬到最后一阶时必须添加到梯子上的 最少 台阶数。

"""
from typing import List


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        last = 0
        count = 0
        for r in rungs:
            add = 0 if r - last <= dist else (r - last) // dist
            if add > 0:
                if (r - last) % dist == 0:
                    add -= 1
            count += add
            last = r
        return count


if __name__ == "__main__":
    test = Solution()

    print(test.addRungs([3],1))
    print(test.addRungs([1,3,5,10],2))
    print(test.addRungs([4,6],1))

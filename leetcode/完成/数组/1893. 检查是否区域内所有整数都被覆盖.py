# -*- coding:utf-8 -*-
# @author :litao
# @Time :2021/7/23 16:23
from typing import List
"""
给你一个二维整数数组 ranges 和两个整数 left 和 right 。每个 ranges[i] = [starti, endi] 表示一个从 starti 到 endi 的 闭区间 。

如果闭区间 [left, right] 内每个整数都被 ranges 中 至少一个 区间覆盖，那么请你返回 true ，否则返回 false 。

已知区间 ranges[i] = [starti, endi] ，如果整数 x 满足 starti <= x <= endi ，那么我们称整数x 被覆盖了。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-if-all-the-integers-in-a-range-are-covered
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # nums = []
        # for lis in ranges:
        #     nums.extend(range(lis[0],lis[1]+1))
        #
        # for i in range(left,right+1):
        #     if i not in nums:
        #         return False
        #
        # return True

        diff = [0] * 52  # 差分数组
        for l, r in ranges:
            diff[l] += 1
            diff[r + 1] -= 1
        # 前缀和
        curr = 0
        for i in range(1, 51):
            curr += diff[i]
            if left <= i <= right and curr <= 0:
                return False
        return True

if __name__ == "__main__":
    test = Solution()
    print(test.isCovered([[1,10],[20,22],[30,32]],2,5))



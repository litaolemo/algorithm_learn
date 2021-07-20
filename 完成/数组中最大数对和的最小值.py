# -*- coding:utf-8 -*-
# @author :litao
# @Time :2021/7/20 10:08

# 1877. 数组中最大数对和的最小值
"""
一个数对 (a,b) 的 数对和 等于 a + b 。最大数对和 是一个数对数组中最大的 数对和 。

比方说，如果我们有数对 (1,5) ，(2,3) 和 (4,4)，最大数对和 为 max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8 。
给你一个长度为 偶数 n 的数组 nums ，请你将 nums 中的元素分成 n / 2 个数对，使得：

nums 中每个元素 恰好 在 一个 数对中，且
最大数对和 的值 最小 。
请你在最优数对划分的方案下，返回最小的 最大数对和 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimize-maximum-pair-sum-in-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

from typing import List

from execute_time import print_execute_time


@print_execute_time
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        new_list = sorted(nums)
        count = len(nums)
        max_num = 0
        for i in range(count // 2):
            max_num = max(max_num,new_list[i]+new_list[count-1-i])

        return max_num


if __name__ == "__main__":
    test = Solution()
    print(test.minPairSum([3, 5, 2, 3]))
    # print(test.minPairSum([3,5,4,2,4,6]))
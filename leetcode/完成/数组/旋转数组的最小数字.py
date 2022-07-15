# -*- coding:utf-8 -*-
# @author :litao
# @Time :2021/7/28 15:09
"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        # low, high = 0, len(numbers) - 1
        # while low < high:
        #     pivot = low + (high - low) // 2
        #     if numbers[pivot] < numbers[high]:
        #         high = pivot
        #     elif numbers[pivot] > numbers[high]:
        #         low = pivot + 1
        #     else:
        #         high -= 1
        # return numbers[low]

        lastnum = numbers[0]
        for i in numbers:
            if i < lastnum:
                return i
            lastnum = i
        return numbers[0]
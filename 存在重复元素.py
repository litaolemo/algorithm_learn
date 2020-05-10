"""
给定一个整数数组，判断是否存在重复元素。

如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        exits_dic = {}
        for num in nums:
            if not exits_dic.get(num):
                exits_dic[num] = 1
            else:
                return True
        return False

test = Solution()
print(test.containsDuplicate([1,2,3,1]))
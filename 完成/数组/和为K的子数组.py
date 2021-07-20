# -*- coding:utf-8 -*-
# @Time : 2020/5/15 16:23 
# @Author : litao
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {}
        count_true = 0
        for count, num in enumerate(nums):
            res = dic.get(k - num)
            if res == num:
                continue
            if res is None:
                dic[num] = count
            else:
                count_true += 1
        return count_true

test = Solution()
# print(test.twoSum([2,7,11,15],9))
# print(test.twoSum([3,2,4],6))
print(test.subarraySum([1,2,3],3))
# -*- coding:utf-8 -*-
# @Time : 2020/5/14 16:58 
# @Author : litao
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # count = nums.count(0)
        # if count > 0:
        #     for c in range(count):
        #         nums.remove(0)
        #         nums.append(0)

        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1

test = Solution()
print(test.moveZeroes([0,1,0,3,12]))
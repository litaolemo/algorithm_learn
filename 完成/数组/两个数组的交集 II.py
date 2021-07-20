# -*- coding:utf-8 -*-
# @Time : 2020/5/14 16:36 
# @Author : litao
from typing import List
class Solution:
    def intersect(self, nums1, nums2):
        dic = {}
        dic_list = []
        for i in nums1:
            if not dic.get(i):
                dic[i] = 1
            else:
                dic[i] += 1
        for i in nums2:
            res =dic.get(i)
            if res is not None:
                if res >= 1:
                    dic[i] -= 1
                    dic_list.append(i)
                else:
                    dic.pop(i)
        return dic_list

test = Solution()
print(test.intersect([1,2,2,1],[2]))
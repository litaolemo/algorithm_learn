# -*- coding:utf-8 -*-
# @Time : 2020/5/15 16:17 
# @Author : litao
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1


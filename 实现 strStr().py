# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 17:50
# @Author  : litao
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0:
            return 0
        try:
            return haystack.index(needle)
        except:
            return -1
# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 15:58
# @Author  : litao
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = ''.join(re.findall(r'[a-zA-Z0-9]+', s)).lower()
        return p == p[::-1]

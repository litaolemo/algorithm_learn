# -*- coding:utf-8 -*-
# @Time : 2020/5/15 16:09 
# @Author : litao
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        str_x = str(x)
        x = ''
        if str_x[0] == '-':
            x += '-'
        x += str_x[len(str_x) - 1::-1].lstrip("0").rstrip("-")
        x = int(x)
        if -2 ** 31 < x < 2 ** 31 - 1:
            return x
        return 0
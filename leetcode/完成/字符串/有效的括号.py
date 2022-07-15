# -*- coding:utf-8 -*-
# @Time : 2020/4/20 19:05 
# @Author : litao
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        zhan = [""]
        for single in s:
            if zhan[-1] == "(" and single == ")":
                zhan.pop()
            elif zhan[-1] == "[" and single == "]":
                zhan.pop()
            elif zhan[-1] == "{" and single == "}":
                zhan.pop()
            else:
                zhan.append(single)
        return True if len(zhan) == 1 else False

test =Solution()
print(test.isValid("()[]{}"))
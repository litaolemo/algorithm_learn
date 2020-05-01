# -*- coding:utf-8 -*-
# @Time : 2020/4/30 17:02 
# @Author : litao
class Solution(object):
    def loop(self,n):
        n_str = str(n)
        num = 0
        for s in n_str:
            num += int(s) * int(s)
        # print(num)
        if num == 1:
            return True
        elif num == 4:
            return False
        else:
            return self.loop(num)

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = self.loop(n)
        return res

test = Solution()
print(test.isHappy(19))
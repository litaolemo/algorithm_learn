# -*- coding:UTF-8 -*-
# @Time  : 2021/3/20 10:25
# @File  : 回文数.py
# @email : litao@chanct.com
# @author : litao

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x == 10:
            return False
        if 0 <= x <= 9:
            return True
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            if revertedNumber == 0:
                return False
            x = int(x/10)
            if x == revertedNumber or revertedNumber == int(x/10):
                return True
        return False


test = Solution()
print(test.isPalindrome(100))
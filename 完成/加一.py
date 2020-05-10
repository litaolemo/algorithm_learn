# -*- coding:utf-8 -*-
# @Time : 2020/5/6 18:22 
# @Author : litao
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # digits = [str(x) for x in digits]
        # str_to_int = str(int("".join(digits)) + 1)
        # return [i for i in str_to_int]
        long = len(digits) - 1
        digits[long] += 1
        for l in range(long):
            if l < long:
                pos = long-l
                if digits[pos] == 10:
                    digits[pos-1] += 1
                    digits[pos] = 0
                else:
                    return digits
        if digits[0] == 10:
            digits.insert(0, 1)
            digits[1] = 0

        return digits


test = Solution()
# print(test.plusOne([1,2,3]))
print(test.plusOne([9,9,9]))
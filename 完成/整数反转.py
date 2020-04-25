# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
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
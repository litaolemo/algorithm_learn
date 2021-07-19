# -*- coding:utf-8 -*-
# @author :litao
# @Time :2021/7/19 13:59

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        r = x
        while r > x / r:
            r = (r + x / r) // 2
        return int(r)

if __name__ == "__main__":
    print(Solution().mySqrt(100))
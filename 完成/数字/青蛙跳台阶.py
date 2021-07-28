# -*- coding:utf-8 -*-
# @author :litao
# @Time :2021/7/28 14:39
"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        last_value = 0
        count = 1
        tmp = 1
        res = 1
        while count <= n:
            res = res + last_value
            last_value = tmp
            tmp = res
            count += 1
            # print(res)
        return res

if __name__ == "__main__":
    test = Solution()
    # print(test.numWays(1))
    # print(test.numWays(2))
    # print(test.numWays(3))
    # print(test.numWays(4))
    # print(test.numWays(5))
    print(test.numWays(6))
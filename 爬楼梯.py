"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。
"""
import functools


class Solution:
    @functools.lru_cache(100)
    def climbStairs(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        return self.climbStairs(n - 1) + self.climbStairs(n - 2) if n > 2 else n
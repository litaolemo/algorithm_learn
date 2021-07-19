# -*- coding:utf-8 -*-
# @author :litao
# @Time :2021/7/19 16:14
# 给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)
        for i in range(n):
            try:
                ans += max(0,prices[i+1]-prices[i])
            except:
                pass
        return ans


if __name__ == "__main__":
    test = Solution()
    print(test.maxProfit())
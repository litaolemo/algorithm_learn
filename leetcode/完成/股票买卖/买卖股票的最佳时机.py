class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        first = 0
        last = len(prices) - 1

        # range_prices = list(range(last+1))
        # new_lsit = list(zip(prices,range_prices))
        # new_lsit = (sorted(new_lsit,key=lambda d: (d[0]),reverse=True))
        # print(new_lsit)
        # while first < last:
        #     end = last
        #     while end > first:
        #         # print(new_lsit[first],new_lsit[end])
        #         first_value, first_time = new_lsit[first]
        #         end_value, end_time = new_lsit[end]
        #         if end_value < first_value and first_time > end_time:
        #             dif = first_value - end_value
        #             print(dif)
        #             if first_value > new_lsit[first + 1][0] and dif >= new_lsit[first + 1][0] and res < dif:
        #                 return dif
        #             else:
        #                 if res < dif:
        #                     res = dif
        #         end -= 1
        #     first += 1
        # return res

        min_price = prices[0]
        max_price = 0
        for price in prices[1:]:
            min_price = min(price,min_price)
            max_price = max(max_price,price-min_price)
        return max_price

test = Solution()
print(test.maxProfit([3,2,6,5,0,3]))


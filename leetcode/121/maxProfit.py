#coding=utf-8

class Solution:
    def maxProfit(self, prices: list) -> int:
        if not prices:
            return 0
        # res[i][0]表示最小股价  res[i][1]表示利润最大值
        res = [[0 for i in range(2)] for i in range(len(prices))]
        res[0][0] = prices[0]
        for i in range(1, len(prices)):
            res[i][0] = min(res[i-1][0], prices[i])
            res[i][1] = max(res[i-1][1], prices[i] - res[i-1][0])
        return res[len(prices) - 1][1]

prices = [7,1,5,3,6,4]
s = Solution()
res = s.maxProfit(prices)
print(res)

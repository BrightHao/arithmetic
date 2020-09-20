class Solution:
    def maxProfit(self, prices: list, fee: int) -> int:
        n = len(prices)
        pro = [[0 for i in range(2)] for j in range(n)]
        pro[0][1] = -prices[0]
        pro[0][0] = 0
        for i in range(1, n):
            pro[i][1] = max(pro[i-1][0] - prices[i], pro[i-1][1])
            pro[i][0] = max(pro[i-1][1] + prices[i] - fee, pro[i-1][0])
        return max(pro[n-1])

    # 节省空间
    def maxProfit1(self, prices: list, fee: int) -> int:
        n = len(prices)
        buy1 = -prices[0]
        sell1 = 0
        for i in range(1, n):
            buy1, sell1 = max(sell1 - prices[i], buy1), max(buy1 + prices[i] - fee, sell1)
        return buy1 if buy1 > sell1 else sell1

arr = [1, 3, 2, 8, 4, 9]
s = Solution()
res = s.maxProfit(arr, 2)
print(res)

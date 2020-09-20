class Solution:
    def maxProfit(self, prices: int) -> int:
        if not prices: return 0
        n = len(prices)
        pro = [[0 for i in range(3)] for j in range(n)]
        pro[0][0] = 0  # 可以买
        pro[0][1] = -prices[0]  # 冷冻期
        pro[0][2] = -prices[0]  # 手上有，可以卖

        for i in range(1, n):
            pro[i][1] = max(pro[i-1][2] + prices[i], pro[i-1][1])  # 卖出
            pro[i][0] = max(pro[i-1][1], pro[i-1][0])  # 冷冻期解冻
            pro[i][2] = max(pro[i-1][0] - prices[i], pro[i-1][2])  # 买入
        print(pro)
        return max(pro[n-1])

a = [1,2]
s = Solution()
res = s.maxProfit(a)
print(res)

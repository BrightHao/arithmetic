class Solution:
    # 空间复杂度需优化
    def maxProfit(self, k: int, prices: list) -> int:
        if not prices: return 0
        if k > len(prices): return self.greedy(prices)

        n = len(prices)
        pro = [[[0 for _ in range(k+1)] for _ in range(2)] for _ in range(n)]
        
        for i in range(n):
            for kk in range(k+1):
                pro[i][1][kk] = -prices[i]

        for p in range(1, n):
            for kk in range(k+1):
                pro[p][0][kk] = max(pro[p-1][0][kk], pro[p-1][1][kk-1] + prices[p] if kk != 0 else pro[p-1][0][kk]) # 卖
                pro[p][1][kk] = max(pro[p-1][1][kk], pro[p-1][0][kk] - prices[p]) # 买
        return max(pro[n-1][0])

    # 处理k过大导致超时的问题，用贪心解决
    def greedy(self, prices):
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res

a = [7,1,5,3,6,4]
s = Solution()
res = s.maxProfit(2, a)
print(res)

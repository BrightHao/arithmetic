class Solution:
    def maxProfit(self, prices: list) -> int:
        n = len(prices)
        pro = [[0 for i in range(2)] for j in range(n)]
        pro[0][1] = -prices[0]
        pro[0][0] = 0
        for i in range(1, n):
            pro[i][1] = max(pro[i-1][0] - prices[i], pro[i-1][1])
            pro[i][0] = max(pro[i-1][1] + prices[i], pro[i-1][0])
        return max(pro[n-1])

    # 节省空间
    def maxProfit1(self, prices: list) -> int:
        n = len(prices)
        buy1 = -prices[0]
        sell1 = 0
        for i in range(1, n):
            buy1, sell1 = max(sell1 - prices[i], buy1), max(buy1 + prices[i], sell1)
        return buy1 if buy1 > sell1 else sell1
    
    # 贪心算法
    def greedy(self, prices: list) -> int:
        n = len(prices)
        sum = 0
        for i in range(1, n):
            if prices[i-1] < prices[i]:
                sum += prices[i] - prices[i-1]
        return sum

arr = [7,1,5,3,6,4]
s = Solution()
res1 = s.maxProfit(arr)
res2 = s.greedy(arr)
print(f"经典递归结果：{res1}  贪心算法结果：{res2}")

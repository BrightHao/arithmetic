class Solution:
    def maxProfit(self, prices: list) -> int:
        if not prices: return 0
        l = len(prices)
        MP = [[[0 for k in range(2)] for j in range(3)] for i in range(l)]
        res = 0

        MP[0][0][0], MP[0][0][1] = 0, -prices[0]  # 第一次没买，第一次买了
        MP[0][1][0], MP[0][1][1] = -prices[0], -prices[0]
        MP[0][2][0], MP[0][2][1] = -prices[0], -prices[0]

        for i in range(1, l):
            MP[i][0][1] = max(MP[i-1][0][1], MP[i-1][0][0] - prices[i])
            MP[i][1][0] = max(MP[i-1][1][0], MP[i-1][0][1] + prices[i])
            MP[i][1][1] = max(MP[i-1][1][1], MP[i-1][1][0] - prices[i])
            MP[i][2][0] = max(MP[i-1][2][0], MP[i-1][1][1] + prices[i])
            print(MP[i])     
        return max(MP[l-1][0][0], MP[l-1][2][0], MP[l-1][1][0])

    def maxProfit2(self, prices: list) -> int:
        """节省空间"""
        if not prices: return 0
        l = len(prices)
        res = 0

        p00 = 0
        # p01 
        p01, p10, p11, p20 = -prices[0], -prices[0], -prices[0], -prices[0]

        for i in range(1, l):
            p01, p10, p11, p20 = max(p01, p00 - prices[i]), max(p10, p01 + prices[i]), max(p11, p10 - prices[i]), max(p20, p11 + prices[i])   
        return max(p00, p10, p20)

t = [2,1,4]
s = Solution()
res = s.maxProfit2(t)
print(res)

class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0 for i in range(n+1)]
        res[0], res[1] = 1, 1
        for j in range(2, n+1):
            res[j] = res[j-1] + res[j-2]
        return res[n]

#coding=utf-8
# DP解法

class Solution():
    def longest_seq(self, str1, str2):
        M = len(str1) + 1
        N = len(str2) + 1
        dp = [["" for i in range(M)] for j in range(N)]
        for i in range(1, N):
            for j in range(1, M):
                if str1[j-1] == str2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + str1[j-1]
                else:
                    dp[i][j] = dp[i-1][j] if len(dp[i-1][j]) > len(dp[i][j-1]) else dp[i][j-1]
        return dp[N-1][M-1]


if __name__ == "__main__":
    str1 = "1A2C3D4B56"
    str2 = "B1D23CA45B6A"
    # str1 = "BDCABA"
    # str2 = "ABCBDAB"
    s = Solution()
    res = s.longest_seq(str1, str2)
    print(res)

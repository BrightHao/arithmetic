class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == s[::-1]: return s
        n = len(s)
        index = 1
        for i in range(n):
            num = i + 1
            if 2*num <= n and s[:num] == s[num:2*num][::-1]:
                index = 2*num
            if 2*num+1 <= n and s[:num+1] == s[num:2*num+1][::-1]:
                index = 2*num+1
        return s[index:][::-1] + s

string = "aaaaa"
s = Solution()
res = s.shortestPalindrome(string)
print(res)

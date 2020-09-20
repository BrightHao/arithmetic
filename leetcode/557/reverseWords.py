class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        for i in range(len(l)):
            l[i] = l[i][::-1]
        return " ".join(l)

t = "I am a cool boy and I love a beautiful girl"
s = Solution()
res = s.reverseWords(t)
print(res)

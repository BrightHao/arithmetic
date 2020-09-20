#coding=utf-8
# 递归解法

class Solution():
    res = ""

    def longest_seq(self, str1, str2):
        return self.loop('', str1, str2)

    def loop(self, combin, leftStr, rightStr):
        if not leftStr and len(combin) > len(self.res):
            self.res = combin
            return
        for i in range(len(leftStr)):
            cur = leftStr[i]
            if cur in rightStr:  # 还有相同的字符，继续遍历下一层
                j = rightStr.index(cur)
                tmp = self.loop(combin+cur, leftStr[i+1:], rightStr[j+1:])
            elif len(combin) > len(self.res):  # 该字符遍历完毕
                self.res = combin

if __name__ == "__main__":
    str1 = "1A2C3D4B56"
    str2 = "B1D23CA45B6A"
    solution = Solution()
    solution.longest_seq(str1, str2)
    res = solution.res
    print(res) if res else print(-1)

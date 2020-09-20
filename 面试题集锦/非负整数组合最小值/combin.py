class Solution():
    def combin(self, nums):
        zero = []
        new = []
        for i in nums:
            if i == 0:
                zero.append("0")
            else:
                new.append(str(i))
        new.sort()
        if not new:
            return 0
        tmp = ''.join(zero) if len(zero) == 1 else ""
        return new[0] + tmp + ''.join(new[1:])

s = Solution()
res = s.combin([10, 0, 2])
print(res)

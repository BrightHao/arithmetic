class Solution:
    def house(self , person):
        mini = 1
        n = len(person)
        res = [1 for i in range(n)]
        res[0] = 1
        for i in range(1, n):
            cur = 0
            if person[i] > person[i-1]:  # 比前者大
                cur = res[i-1] + 1
            elif person[i] < person[i-1]:  # 比前者小
                if i + 1 < n and person[i+1] < person[i]:  # 比后者大
                    cur = res[i-1] - 1
                else:  # 比后者小
                    cur = mini if res[i-1] > mini else mini - 1
            else:  # 与前者一样
                cur = mini
            mini = mini if mini < cur else cur
            res[i] = cur
        return sum(res) + n * (1 - mini)

a = [3,2,4]
s = Solution()
res = s.house(a)
print(res)

class Solution:
    result = ""

    def getPermutation(self, n: int, k: int) -> str:
        arr = [i for i in range(1, n+1)]
        return self.find(k, arr)

    # 输出n!
    def cal(self, n: int) -> int:
        if n == 0: return 1
        res = 1
        for i in range(2, n+1):
            res *= i
        return res

    def find(self, n: int, ll: list) -> str:
        # 如果是123 找第三个
        # 因为2!*1 <= 3 < 2!*2  取index=1的2  3-2=1 12  将1和12作为参数继续递归
        if len(ll) == 0: return self.result
        unit = self.cal(len(ll)-1)
        for i in range(len(ll)-1, -1, -1):
            if n > unit * i:
                print(f"取{ll}全排序的第{i}个：{ll[i]}")
                self.result += str(ll[i])
                return self.find(n-unit*i, ll[:i] + ll[i+1:])

if __name__ == "__main__":
    s = Solution()
    res = s.getPermutation(5, 24)
    print(res)

class Solution:
    def minimumTotal(self, triangle: list) -> int:
        res = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        return res[0]


tri = [[2],[3,4],[6,5,7],[4,1,8,3]]
s = Solution()
res = s.minimumTotal(tri)
print(res)

class Solution:
    def canJump(self, nums: list) -> bool:
        index = 0 
        for i in range(len(nums)-1):
            if index < i: return False  # 该位置不可达
            index = max(index, i + nums[i])
        return index >= len(nums) - 1


a = [2, 0, 1, 4, 0, 0, 3]
s = Solution()
res = s.canJump(a)
print(res)

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        dd = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            res = dd.get(temp)
            if res != None:
                return [res, i]
            dd[nums[i]] = i
        return []

s = Solution()
res = s.twoSum([2,7,11,15], 9)
print(res)

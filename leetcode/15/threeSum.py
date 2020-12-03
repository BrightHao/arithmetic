"""判断其中是否又三数之和等于0"""

class Solution:
    def threeSum1(self, nums: list) -> list:
        if len(nums) < 3: return []
        nums.sort()
        res = set()
        for i, x in enumerate(nums[:-2]):
            if i >= 1 and x == nums[i-1]:
                continue
            d = {}
            for y in nums[i+1:]:
                if y not in d:
                    d[-x-y] = 1
                else:
                    res.add((x, y, -x-y))
        return list(map(list, res))

    def threeSum2(self, nums: list) -> list:
        if len(nums) < 3: return []
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0: l += 1
                elif s > 0: r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r-=1
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.threeSum2([-1, 0, 1, 2, -1, -4])
    print(res)

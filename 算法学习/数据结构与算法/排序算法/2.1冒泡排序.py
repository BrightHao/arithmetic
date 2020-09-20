"""
1.遍历列表
2.从后往前比较未排序的数，如果为逆序则交换位置
3.如果在一趟中没有交换元素，则说明列表全部为正确顺序
时间复杂度： 最坏情况为O(n^2)  平均时间复杂度也是 O(n^2)
"""
import time


t = time.time()

ll = [10, 5, 1, 4, 14, 85, 21, 7, 15, 5, 48, 48, 46, 88, 84, 254, 8498, 4984, 5, 51651, 651, 6516, 156, 1651, 651, 61,
      61, 651, 651, 65]
n = len(ll)

# 从小到大排序
for i in range(1, n):
    j = n - 1
    swap = False
    while j > i:
        if ll[j] < ll[j-1]:
            ll[j], ll[j-1] = ll[j-1], ll[j]
            swap = True
        j -= 1
    if not swap:
        break
print(ll)


# 从大到小排序
for i in range(1, n):
    j = n - 1
    swap = False
    while j >= i:
        if ll[j] > ll[j-1]:
            ll[j], ll[j-1] = ll[j-1], ll[j]
            swap = True
        j -= 1
    if not swap:
        break
print(ll)

print("所用时间： ", t - time.time())

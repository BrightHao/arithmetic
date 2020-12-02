"""
基于直接插入排序
在比较前面已经排好序的部分的时候，使用折中比较法，减少了比较的次数，约为 O(nlog2n)
时间复杂度： O(n^2)
"""
import time
t1 = time.time()


# 从小到大排序
ll = [0, 5, 1, 4, 14, 85, 21, 7, 15, 5, 48, 48, 46, 88, 84, 254, 8498, 4984, 5, 51651, 651, 6516, 156, 1651, 651, 61,
      61, 651, 651, 65]
print("原列表： ", ll)
for i in range(1, len(ll)):
    num = ll[i]  # 记录该元素
    if num < ll[i - 1]:  # 如果他比他前面的小，就寻找该插入的位置    比他前面的大，说明当前顺序正常，无需排序
        low = 0
        high = i - 1  # 折中的范围，即已经排好序的部分
        while low <= high:
            mid = (low + high) // 2
            if ll[mid] > num:  # 中间数大于它，从中间数往后全部后移一位，然后中间位置让给它
                high = mid - 1
            else:
                low = mid + 1
        for j in range(i, high, -1):  # 整体往后移，腾出空间
            ll[j] = ll[j - 1]
        ll[high + 1] = num
print("正序排列： ", ll)


# 从大到小排序
for i in range(1, len(ll)):
    num = ll[i]  # 记录该元素
    if num > ll[i - 1]:  # 如果他比他前面的小，就寻找该插入的位置    比他前面的小，说明当前顺序正常，无需排序
        low = 0
        high = i - 1  # 折中的范围，即已经排好序的部分
        while low <= high:
            mid = (low + high) // 2
            if ll[mid] < num:  # 中间数大于它，从中间数往后全部后移一位，然后中间位置让给它
                high = mid - 1
            else:
                low = mid + 1
        for j in range(i, high, -1):  # 整体往后移，腾出空间
            ll[j] = ll[j - 1]
        ll[high + 1] = num
print("倒序排列： ", ll)


print("所用时间: ", time.time() - t1, "秒")

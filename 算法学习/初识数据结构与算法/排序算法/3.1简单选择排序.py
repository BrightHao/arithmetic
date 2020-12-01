"""
简单选择排序
每一趟遍历选取后面 (n-i+1) 个关键字的最小值，放置到 i 的位置
时间复杂度： O(n^2)
"""

def simple_select_sort(ll):
    n = len(ll)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if ll[j] < ll[min]:
                min = j
        ll[min], ll[i] = ll[i], ll[min]

ll = [10, 5, 1, 4, 14, 85, 21, 7, 15, 5, 48, 48, 46, 88, 84, 254, 8498, 4984, 5, 51651, 651, 6516, 156, 1651, 651, 61,
      61, 651, 651, 65]
simple_select_sort(ll)
print(ll)

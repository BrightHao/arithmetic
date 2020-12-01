"""
性能分析：
空间效率：O(1)
时间效率：最好情况下，表中元素已经有序，只需要比较不需要移动，比较次数为n-1，为O(1)
          最坏情况下，表中元素刚好逆向，需要比较n-1次，需要移动1+2+...+n-1次，一共n-1 + (1+n-1)/2*(n-1) 约为： n^2/2
           所以平均移动次数为：n^2/4  所以 直接插入排序的时间复杂度为 O(n^2)
实现步骤：
1.遍历列表元素，记录该元素的值
2.从后往前查找待插入的位置
3.把该元素填充到该插入的位置
"""
import time
t1 = time.time()


# 从小到大排序
ll = [0, 5, 1, 4, 14, 85, 21, 7, 15, 5, 48, 48, 46, 88, 84, 254, 8498, 4984, 5, 51651, 651, 6516, 156, 1651, 651, 61,
      61, 651, 651, 65]
print("原列表： ", ll)
for i in range(1, len(ll)):
    num = ll[i]  # 记录该元素
    if num < ll[i - 1]:  # 如果他比他前面的小，就寻找该插入的位置   比他前面的大，说明当前顺序正常，无需排序
        index = 0
        for j in range(i - 1, -1, -1):
            if num < ll[j]:
                ll[j + 1] = ll[j]  # 把大的元素往后挪
            else:
                break
            index = j
        ll[index] = num
    # print(f"第{i}次排序： ", num, ll)
print("正序排列： ", ll)

# 从大到小排序
for i in range(1, len(ll)):
    num = ll[i]  # 取值
    if num > ll[i - 1]:  # 如果他比他前面的大，就寻找该插入的位置
        index = 0
        for j in range(i - 1, -1, -1):
            if num > ll[j]:
                ll[j + 1] = ll[j]  # 把大的元素往后挪
            else:
                break
            index = j
        ll[index] = num
    # print(f"第{i}次排序： ", num, ll)
print("倒序排列：  ", ll)


print("所用时间: ", time.time() - t1, "秒")

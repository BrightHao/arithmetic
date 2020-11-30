num = int(input())
arr = [int(i) for i in input().split()]
min = 99999  # 最小值
min_ = 99999  # 上面有空值的最小值
res = 1
for i in range(num):
    if 0 < arr[i] < min - 1 or arr[i] == min_ + 1:
        min_ = arr[i]
        res = min_ + 1
    if 0 < arr[i] < min:  # 记录最小值
        min = arr[i]
print(res)

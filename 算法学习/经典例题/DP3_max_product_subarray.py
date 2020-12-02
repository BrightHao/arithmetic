#coding=utf-8
"""
最大字符子串乘积
"""
def maxProduct(array):
    res = array[0]
    maxArr = [array[0] if i == 0 else 0 for i in range(len(array))]
    minArr = [array[0] if i == 0 else 0 for i in range(len(array))]
    for i in range(1, len(array)):
        if array[i] == 0 or array[i-1] == 0:
            maxArr[i] = 0
            minArr[i] = 0
        else:
            maxArr[i] = max(maxArr[i-1] * array[i], minArr[i-1] * array[i], array[i])
            minArr[i] = min(maxArr[i-1] * array[i], minArr[i-1] * array[i], array[i])
        res = max(maxArr[i], res)
    return res

if __name__ == "__main__":
    array = [2, 3, -10, 5, -1]
    res = maxProduct(array)
    print(res)

#coding=utf-8


def my_main(array):
    if not array:
        return 0
    L = len(array)
    # 用于存储最终结果的数组，可以改为一维数组，因为只需要存储上层每个节点的最小值，这里把每个节点的值都计算出来
    max_array = [[0 for j in range(i+1)] for i in range(L)]
    # 初始化第一个位置
    max_array[0][0] = array[0][0]
    # 计算每层第一个位置最小值
    for i in range(1, L):
        max_array[i][0] = max_array[i-1][0] + array[i][0]
    # 计算每层最后一个位置最小值
    for i in range(1, L):
        max_array[i][i] = max_array[i-1][i-1] + array[i][i]
    # 计算中间部分的节点最小值
    for i in range(1, L):
        for j in range(1, i):
            # 每次加上上一层路径的最小值，就是当前节点的最小值；同理，将min换成max就是求最大值；
            max_array[i][j] = min(max_array[i-1][j], max_array[i-1][j-1]) + array[i][j]
    return min(max_array[L-1])

def main(array):
    if not array:
        return 0
    # 用来存储最终结果的数组
    res = array[-1]
    # 从下往上累加，不会存在数组越界的情况
    for i in range(len(array) - 2, -1, -1):
        for j in range(len(array[i])):
            res[j] = min(res[j], res[j+1]) + array[i][j]
    return res[0]


if __name__ == "__main__":
    array = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    # res = my_main(array)
    res = main(array)
    print(res)

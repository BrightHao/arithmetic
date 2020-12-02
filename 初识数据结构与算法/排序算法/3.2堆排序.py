"""
    10
  5    9
3  2  6  8
上图表示为一个大顶堆，父节点大于等于下面的双亲节点

时间复杂度： O(nlog2n)
"""

def down_heapify(tree, i):  # 从上向下进行递归操作   只对一边有效
    l = 2 * i + 1
    r = 2 * i + 2
    print(i, l, r)
    max = i
    if l <= n and tree[l] > tree[max]:
        max = l
    if r <= n and tree[r] > tree[max]:
        max = r
    if max != i:
        tree[i], tree[max] = tree[max], tree[i]
        down_heapify(tree, max)

if __name__ == "__main__":
    ll = [9, 32, 17, 65, 53, 87, 45, 78]
    n = len(ll) - 1  # 8
    max = (n - 1) // 2  # 3
    print(ll)
    for i in range(max, -1, -1):  # 3 2 1 0
        down_heapify(ll, i)
    print(ll)

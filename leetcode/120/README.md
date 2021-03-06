### 题目描述
求三角形最小路径和

给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

### 解题思路
- 1.暴力破解，递归出所有可能性，计算最小值；
- 2.DP法，当前节点的最小值等于前一个位置或者上层的同位置最小值加上当前值；优化：从尾部开始计算，不会有数组跨界的问题。

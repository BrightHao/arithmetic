#coding=utf-8
"""
题目描述：斐波拉契数列，即 fib[0]=1,fib[1]=1,后面的数等于前两数之和,求fib[n]
"""

# 经典解法，递归；时间复杂度：O(2^n)，对于大数字计算十分缓慢！
def recursion(n):
    return 1 if n == 0 or n == 1 else recursion(n-1) + recursion(n-2)

# 动态规划；时间复杂度O(n)，计算快捷
def dynamic(n):
    ans = [1, 1]
    for i in range(2, n + 1):
        ans.append(ans[i-1] + ans[i-2])
    return ans[n]

if __name__ == "__main__":
    # res = recursion(50)
    res = dynamic(50)
    print(res)

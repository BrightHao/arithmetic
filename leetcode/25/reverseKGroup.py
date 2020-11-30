import os
import sys
sys.path.append(os.path.abspath('../struct'))
from single_link_list import SingleLinkList


class Solution:
    def __init__(self, *args):
        self.single_link_list = SingleLinkList(None, *args)
        print("初始化： ", end="")
        self.single_link_list.travel()
    
    def reverseKGroup(self, k):
        start, end, self.next = self, self.single_link_list.head, self.single_link_list.head
        has = 0
        count = 1
        while end:  # 如果本节点不为空
            if count == k:
                prev, cur = start.next, start.next.next  # 从start节点开始
                while not (prev is end):
                    cur.next, prev, cur = prev, cur, cur.next
                start.next.next, start.next, start = cur, prev, start.next

                if not has:
                    self.next = end
                    has = 1

                end = start.next
                count = 1
            else:
                end = end.next  # 指针往下走
                count += 1  # 计数
        self.single_link_list.travel(self.next)


if __name__ == "__main__":
    l = Solution(1, 2, 3, 4, 5, 6, 8, 9)
    l.reverseKGroup(2)

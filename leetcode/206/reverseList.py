import os
import sys
sys.path.append(os.path.abspath('../struct'))
from single_link_list import SingleLinkList

class Solution:
    def __init__(self, *k):
        link_list = SingleLinkList(None, *k)
        print("初始化： ", end=" ")
        link_list.travel()
        self.link_list = link_list

    """记录前驱节点，将指针指向前驱"""
    def reverseList(self, head):
        cur, prev = head, None
        while cur:
            cur.next, cur, prev = prev, cur.next, cur
        self.link_list.travel(prev)

    def travel(self):
        self.link_list.travel()

if __name__ == "__main__":
    ll = Solution(2, 4, 6, 8, 9)
    ll.reverseList(ll.link_list.head)


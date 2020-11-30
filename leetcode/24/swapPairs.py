import os
import sys
sys.path.append(os.path.abspath('../struct'))
from single_link_list import SingleLinkList

class Solution:
    def __init__(self, *k):
        link_list = SingleLinkList(None, *k)
        print("初始化 ", end=" ")
        link_list.travel()
        self.link_list = link_list

    def swapPairs(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a, b = pre.next, pre.next.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        self.link_list.travel(self.next)

    def travel(self):
        self.link_list.travel()

if __name__ == "__main__":
    ll = Solution(2, 4, 6, 8, 9)
    ll.swapPairs(ll.link_list.head)

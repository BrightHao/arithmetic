import os
import sys
sys.path.append(os.path.abspath('../struct'))
from single_link_list import SingleLinkList

class Solution:
    def __init__(self, pos=-1, *args):
        single_link_list = SingleLinkList(None, *args)
        if 0 <= pos <= len(args) - 1:
            count = 0
            cur = single_link_list.head
            while cur != None:
                if count == pos:
                    break
                else:
                    count += 1
                    cur = cur.next
            single_link_list.tail.next = cur
        self.single_link_list = single_link_list
    
    def hasCycle(self, head=None) -> bool:
        """快慢指针解法"""
        head = self.single_link_list.head if not head else head
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


if __name__ == "__main__":
    ll = Solution(4, 3, 5, 7, 8)
    res = ll.hasCycle()
    print(res)
    if not res:
        ll.single_link_list.travel()

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

    def detectCycle(self, head=None):
        head = self.single_link_list.head if not head else head
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                while not (slow is head):
                    slow = slow.next
                    head = head.next
                cur = head
                print(cur.elem, end="->")
                while cur.next != head:
                    cur = cur.next
                    print(cur.elem, end="->")
                print(head.elem)
                break
        return None


if __name__ == "__main__":
    ll = Solution(1, 3, 5, 6, 10, 1, 2)
    ll.detectCycle()

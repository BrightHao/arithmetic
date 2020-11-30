"构建一个单向链表的结构"

class Node:
    """节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkList:
    """单链表"""
    def __init__(self, node=None, *args):
        self.head = node
        self.tail = node
        for i in args:
            self.append(i)

    def is_empty(self):
        """链表是否为空"""
        return self.head is None

    def length(self):
        """链表长度"""
        cur = self.head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self, head=None):
        """遍历整个链表"""
        cur = self.head if not head else head
        while cur != None:
            print(cur.elem, end="->")
            cur = cur.next
        print("NULL")

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self.head
        self.head = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            self.tail = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
           self.add(item)
        elif pos + 1 > self.length():
            self.append(item)
        else:
            count = 0
            cur = self.head
            node = Node(item)
            while count < pos - 1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 先判断此节点是否是头节点
                if pre == None:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                    if cur.next == None:
                        self.tail = pre
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    ll = SingleLinkList(None, 4, 8, 9)
    ll.travel()

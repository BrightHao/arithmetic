"构建一个单向链表的结构"

class Node:
    """节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkList:
    """单向循环链表"""
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        print(cur.elem)

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node
            self.__head = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
           self.add(item)
        elif pos + 1 > self.length():
            self.append(item)
        else:
            count = 0
            cur = self.__head
            node = Node(item)
            while count < pos - 1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.elem == item:  # 找到了节点
                # 头节点
                if cur == self.__head:
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:  # 中间节点
                    pre.next = cur.next
                return
            else:  # 继续向后遍历
                pre = cur
                cur = cur.next
        # 遍历到最后一个节点
        if cur.elem == item:
            if cur.next == cur:
                self.__head = None
            else:
                pre.next = cur.next

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem == item:
            return True
        else:
            return False


if __name__ == "__main__":
    ll = SingleLinkList()
    ll.append(1)
    ll.append(1)
    ll.append(1)
    ll.travel()
    ll.remove(1)
    ll.travel()

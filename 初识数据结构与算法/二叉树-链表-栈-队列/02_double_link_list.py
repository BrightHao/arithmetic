class Node:
    """节点"""
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None


class DoubleLinkList:
    """双链表"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print()

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

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
            cur.next.prev = node
            node.next = cur.next
            cur.next = node
            node.prev = cur

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                if cur.prev == None:  # 删除第一个节点
                    self.__head = cur.next
                    if cur.next:  # 判断链表是否只有一个节点
                        cur.next.pre = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    dll = DoubleLinkList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.insert(5, 546)
    dll.travel()
    print(dll.search(6))
    print(dll.search(5))
    dll.remove(4)
    dll.remove(1)
    dll.travel()

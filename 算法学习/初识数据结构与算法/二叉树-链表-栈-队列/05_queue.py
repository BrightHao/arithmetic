
class Queue:
    """队列"""
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """往队列中添加一个元素"""
        self.items.append(item)

    def dequeue(self):
        """往队列头部删除一个元素"""
        if self.is_empty():
            return None
        else:
            return self.items.pop(0)

    def is_empty(self):
        """判断队列是否为空"""
        return self.items == []

    def size(self):
        """返回元素个数"""
        return len(self.items)


if __name__ == "__main__":
    s = Queue()
    print(s.is_empty())
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
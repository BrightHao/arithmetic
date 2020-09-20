
class Stack:
    """栈"""
    def __init__(self):
        self.__list = []

    def push(self, item):
        """添加一个新的元素item到栈底"""
        self.__list.append(item)

    def pop(self):
        """弹出栈顶元素"""
        self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.is_empty():
            return None
        else:
            return self.__list[-1]

    def is_empty(self):
        """判断堆栈是否为空"""
        return self.__list == []

    def size(self):
        """返回堆栈元素个数"""
        return len(self.__list)

    def show(self):
        """返回堆栈"""
        return self.__list

if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())
    s.push(41)
    s.push(415)
    s.push(4)
    s.push(65)
    print(s.size())
    s.pop()
    s.pop()
    print(s.peek())
    print(s.show())
"""堆栈的模拟表示"""

class Stack:
    def __init__(self):
        self.list = []

    def has(self, item):
        return item in self.list

    def append(self, item: int):
        self.list.append(item)
    
    def pop(self):
        return self.list.pop()

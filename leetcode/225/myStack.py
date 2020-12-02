class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue_in = []
        self.queue_out = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue_in.insert(0, x)
        while self.queue_out:
            self.queue_in.insert(0, self.queue_out.pop())
        self.queue_out = self.queue_in
        self.queue_in = []

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty(): return None
        return self.queue_out.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty(): return None
        return self.queue_out[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue_out

if __name__ == "__main__":
    # Your MyStack object will be instantiated and called as such:
    obj = MyStack()
    obj.push(3)
    obj.push(6)
    obj.push(7)
    obj.push(2)
    param_2 = obj.pop()
    param_3 = obj.top()
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
    param_4 = obj.empty()
    print(param_2, param_3, param_4)

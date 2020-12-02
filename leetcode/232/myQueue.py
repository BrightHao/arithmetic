class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Stack_out = []
        self.Stack_in = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.Stack_in.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty(): return None
        if not self.Stack_out:
            while self.Stack_in:
                self.Stack_out.append(self.Stack_in.pop())
        return self.Stack_out.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty(): return None
        return self.Stack_out[-1] if self.Stack_out else self.Stack_in[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return False if self.Stack_out or self.Stack_in else True

if __name__ == "__main__":
    # Your MyQueue object will be instantiated and called as such:
    obj = MyQueue()
    obj.push(3)
    obj.push(5)
    obj.push(2)
    obj.push(7)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
    print(param_2, param_3, param_4)

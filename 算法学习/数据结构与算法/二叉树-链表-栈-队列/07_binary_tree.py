
class Node:
    """节点"""
    def __init__(self, item):
        self.elem = item
        self.left = None
        self.right = None

class Tree:
    """二叉树"""
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.left is None:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)
            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)

    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node:
                print(cur_node.elem)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)

    def pre_travel(self):
        """先序遍历"""
        self.__preOrder(self.root)

    def __preOrder(self, root):
        """先序遍历"""
        if root is None:
            return
        print(root.elem)
        self.__preOrder(root.left)
        self.__preOrder(root.right)

    def in_travel(self):
        """中序遍历"""
        self.__inOrder(self.root)

    def __inOrder(self, root):
        """中序遍历"""
        if root is None:
            return
        self.__inOrder(root.left)
        print(root.elem)
        self.__inOrder(root.right)

    def post_travel(self):
        """后序遍历"""
        self.__postOrder(self.root)

    def __postOrder(self, root):
        """后序遍历"""
        if root is None:
            return
        self.__postOrder(root.left)
        self.__postOrder(root.right)
        print(root.elem)


if __name__ == "__main__":
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    # tree.pre_travel()
    # tree.in_travel()
    # tree.post_travel()

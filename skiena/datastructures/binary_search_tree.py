from .stack import Stack, StackEmptyError


class BinarySearchTreeNode:
    def __init__(self, value, content=None, parent=None, left=None, right=None):
        self.value = value
        self.content = content
        self.parent = parent
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self._min = None
        self._max = None

    def search(self, value) -> BinarySearchTreeNode:
        """search in O(log h)"""
        node = self.root
        while node:
            if node.value == value:
                return node
            node = node.left if node.value > value else node.right
        raise FileNotFoundError

    def min(self) -> BinarySearchTreeNode:
        """O(log h)"""
        node = self.root
        if not node:
            return None
        while node.left:
            node = node.left
        return node

    def max(self) -> BinarySearchTreeNode:
        """O(log h)"""
        node = self.root
        if not node:
            return None
        while node.right:
            node = node.right
        return node

    def traverse(self, action=lambda node: print(f'#{node.value} -> {node.content}')):
        """O(n)"""
        stack = Stack(implementation='array')

        class StackItem:
            def __init__(self, node: BinarySearchTreeNode, status: int):
                self.node = node
                self.status = status
        stack_item = StackItem(self.root, 0)
        while stack_item:
            if stack_item.node:
                if not stack_item.status:
                    stack.push(stack_item)
                    stack.push(StackItem(node=stack_item.node.left, status=0))
                    stack_item.status = 1
                elif stack_item.status == 1:
                    action(stack_item.node)
                    stack.push(StackItem(node=stack_item.node.right, status=0))
            try:
                stack_item = stack.pop()
            except StackEmptyError:
                stack_item = None

    def insert(self, value, content=None):
        """O(h)"""
        node = BinarySearchTreeNode(value=value, content=content)
        if not self.root:
            self.root = node
        else:
            parent_node = self.root
            while True:
                if parent_node.value >= value:
                    left_child = parent_node.left
                    if left_child:
                        parent_node = left_child
                    else:
                        parent_node.left = node
                        node.parent = parent_node
                        break
                else:
                    right_child = parent_node.right
                    if right_child:
                        parent_node = right_child
                    else:
                        parent_node.right = node
                        node.parent = parent_node
                        break

    def delete(self, node):
        """O(h)"""
        parent_node = node.parent
        if not node.left and not node.right:
            if not parent_node:
                self.root = None
            else:
                if parent_node.left is node:
                    parent_node.left = None
                else:
                    parent_node.right = None
        elif not node.left and node.right:
            if not parent_node:
                self.root = node.right
                self.root.parent = None
            else:
                if parent_node.left is node:
                    parent_node.left = node.right
                    parent_node.left.parent = parent_node
                else:
                    parent_node.right = node.right
                    parent_node.right.parent = parent_node
        elif node.left and not node.right:
            if not parent_node:
                self.root = node.left
                self.root.parent = None
            else:
                if parent_node.left is node:
                    parent_node.left = node.left
                    parent_node.left.parent = parent_node
                else:
                    parent_node.right = node.left
                    parent_node.right.parent = parent_node
        else:
            # find leftmost child on the right subtree
            leftmost_child = node.right
            while leftmost_child.left:
                leftmost_child = leftmost_child.left
            # cut it away from the tree
            if leftmost_child.parent is node:
                node.right = None
            else:
                leftmost_child.parent.left = None
            # attach left subtree to its left
            leftmost_child.left = node.left
            leftmost_child.left.parent = leftmost_child
            # find leftmost_child.right
            # if it has a right child but no left child
            # and then this right child should occupy the leftmost_child's
            # former position
            if leftmost_child.right:
                if leftmost_child.parent is node:
                    pass
                else:
                    leftmost_child.parent.left = leftmost_child.right
                    leftmost_child.parent.left.parent = leftmost_child.parent
            if leftmost_child.parent is not node:
                leftmost_child.right = node.right
            # check if there is actually node.right
            # because if node was the leftmost_child's parent,
            # its right has been set to None
            if leftmost_child.right:
                leftmost_child.right.parent = leftmost_child
            # bind it to the parent_node
            leftmost_child.parent = parent_node
            if parent_node:
                if parent_node.left is node:
                    parent_node.left = leftmost_child
                else:
                    parent_node.right = leftmost_child
            else:
                self.root = leftmost_child

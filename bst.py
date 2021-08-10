class TreeNode:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def successor(self):
        if self.right:
            return self.right.min()

        curr = self
        par = curr.parent
        while par is not None and par.right == curr:
            curr = par
            par = par.parent
        return par

    def predecessor(self):
        if self.left:
            return self.left.max()

        curr = self
        par = curr.parent
        while par is not None and par.left == curr:
            curr = par
            par = par.parent
        return par

    def min(self):
        local_root = self
        while local_root.left is not None:
            local_root = local_root.left
        return local_root

    def max(self):
        local_root = self
        while local_root.right is not None:
            local_root = local_root.right
        return local_root


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def inorder_walk(self):
        """ Prints every element in the tree in sorted order"""
        BinarySearchTree._inorder_walk(self.root)

    @staticmethod
    def _inorder_walk(local_root):
        if local_root is not None:
            BinarySearchTree._inorder_walk(local_root.left)
            print(local_root.key, end=" ")
            BinarySearchTree._inorder_walk(local_root.right)

    def search(self, key):
        """ Return the node which contains the specified key """
        local_root = self.root
        while local_root is not None or local_root is not key:
            if key < local_root:
                local_root = local_root.left
            else:
                local_root = local_root.right
        return local_root

    def recursive_search(self, key):
        return BinarySearchTree._recursive_search(self.root, key)

    @staticmethod
    def _recursive_search(local_root, key):
        if local_root is None or local_root.key == key:
            return local_root
        elif key < local_root.key:
            return BinarySearchTree.search(local_root.left, key)
        else:
            return BinarySearchTree.search(local_root.right, key)

    def min(self):
        return self.root.min() if self.root else None

    def max(self):
        return self.root.max() if self.root else None

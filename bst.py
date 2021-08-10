class TreeNode:
    def __init__(self, key, parent = None, left = None, right = None):
        self.key = None
        self.parent = parent
        self.left = left
        self.right = right


    def successor(self):
        if self.right:
            return self.right.min()

        curr = self
        par = curr.parent
        while par != None and par.right == curr:
            curr = par
            par = par.parent
        return par

    def predecessor(self):
        if self.left:
            return self.left.max()

        curr = self
        par = curr.parent
        while par != None and par.left == curr:
            curr = par
            par = par.parent
        return par

    def min(self):
        localroot = self
        while localroot.left != None:
            localroot = localroot.left
        return localroot

    def max(self):
        localroot = self
        while localroot.right != None:
            localroot = localroot.right
        return localroot

    def _recursive_search(self, key):
        pass



class BinarySearchTree:
    def __init__(self):
        self.root = None

    def inorder_walk(self):
        """ Prints every element in the tree in sorted order"""
        BinarySearchTree._inorder_walk(self.root)

    @staticmethod
    def _inorder_walk(localroot):
        if localroot != None:
            BinarySearchTree._inorder_walk(localroot.left)
            print(localroot.key, end = " ")
            BinarySearchTree._inorder_walk(localroot.right)

    def search(self, key):
        """ Return the node which contains the specified key """
        localroot = self.root
        while localroot != None or localroot != key:
            if key < localroot:
                localroot = localroot.left
            else:
                localroot = localroot.right
        return localroot


    def recursive_search(self, key):
        return BinarySearchTree._recursive_search(self.root, key)

    @staticmethod
    def _recursive_search(localroot, key):
        if localroot == None or localroot.key == key:
            return localroot
        elif key < localroot.key:
            return BinarySearchTree.search(localroot.left, key)
        else:
            return BinarySearchTree.search(localroot.right, key)

    def max(self):
        return self.root.min() if self.root else None

    def max(self):
        return self.root.max() if self.root else None
class TreeNode:
    def __init__(self, key, parent = None, left = None, right = None):
        self.key = None
        self.parent = parent
        self.left = left
        self.right = right


    def successor(self):
        pass

    def predecessor(self):
        pass


    def _min(self):
        pass

    def _max(self):
        while

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
            print(localroot.key)
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
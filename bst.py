class TreeNode:
    def __init__(self, key, left = None, right = None):
        self.key = None
        self.left = left
        self.right = right


    def successor(self):
        pass

    def predecessor(self):
        pass


    def _min(self):
        pass

    def _max(self):
        pass

    def _search(self, key):
        pass

    def _recursive_search(self, key):
        pass



class BinarySearchTree:
    def __init__(self):
        self.root = None

    def inorder_walk(self):
        """ Prints every element in the tree in sorted order"""
        self._inorder_walk(self.root)

    @staticmethod
    def _inorder_walk(localroot):
        if localroot != None:
            BinarySearchTree._inorder_walk(localroot.left)
            print(localroot.key)
            BinarySearchTree._inorder_walk(localroot.right)
class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left  # Changed from left_child to left
        self.right = right  # Changed from right_child to right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = TreeNode(data)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if data < current_node.data:
                    if current_node.left is None:
                        current_node.left = new_node
                        return
                    else:
                        current_node = current_node.left
                elif data > current_node.data:
                    if current_node.right is None:
                        current_node.right = new_node
                        return
                    else:
                        current_node = current_node.right

    def search(self, data):
        current_node = self.root
        while current_node is not None:
            if data == current_node.data:
                return True
            elif data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False


# Create an instance of BinarySearchTree
bst = BinarySearchTree()
bst.insert("Pride and Prejudice")

# Now calling search on the bst instance
print(bst.search("Pride and Prejudice"))  # This should return True

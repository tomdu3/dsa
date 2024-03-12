class BinarySearchTree:
  def __init__(self):
    self.root = None

  def in_order(self, current_node):
    # Check if current_node exists
    if current_node:
      # Call recursively with the appropriate half of the tree
      self.in_order(current_node.left_child)
      # Print the value of the current_node
      print(current_node.data)
      # Call recursively with the appropriate half of the tree
      self.in_order(current_node.right_child)
  
bst = CreateTree()
bst.in_order(bst.root)
# Binary Search Tree (BST)
- [https://en.wikipedia.org/wiki/Binary_search_tree](https://en.wikipedia.org/wiki/Binary_search_tree)
![binary-search-tree](./docs/Binary_search_tree.svg)


## Definition
- Binary search tree is a tree where each node has 0, 1 or 2 children
- **Left subtree** of a node:
  - values **less** than the node itself
- **Right subtree** of a node:
  - values **greater** than the node itself
- Left and right subtrees must be binary search trees

## Implementations

```python
class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left_child = left
        self.right_child = right
```

```python
class BinarySearchTree:
    def __init__(self):
        self.root = None
```

### Searching
```python
def search(self, search_value):
    current_node = self.root
    while current_node:
        if search_value == current_node.data:
            return True
        elif search_value < current_node.data:
            current_node = current_node.left_child
        else:
            current_node = current_node.right_child
    return False
```

### Inserting
```python
def insert(self, data):
    new_node = TreeNode(data)
    if not self.root:
        self.root = new_node
        return
    else:
        current_node = self.root
        while True:
            if data < current_node.data:
                if current_node.left_child is None:
                    current_node.left_child = new_node
                    return
                else:
                    current_node = current_node.left_child
            elif data > current_node.data:
                if current_node.right_child is None:
                    current_node.right_child = new_node
                    return
                else:
                    current_node = current_node.right_child
```

### Deleting
If Node has:
- **No children**:
  - delete it
- **One child**:
  - delete it
  - connect the child with node's parent
- **Two children**:
  - replace it with its successor:
    - the node with the smallest value greater than the value of the node
  - find the successor:
    - visit the right child
    - keep visiting the left nodes until the end
    - if the successor has a right child:
      - child becomes the left child of successor's parent

## Uses
- Order lists efficiently
- Much faster at searching than arrays and linked lists
- Much faster at inserting and deleting than arrays
- Used to implement more advanced data structures:
  - dynamic sets
  - lookup tables
  - priority queues

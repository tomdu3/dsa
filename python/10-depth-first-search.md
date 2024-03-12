#Depth First Search (DFS)

## Tree/graph traversal
- process of visiting **all nodes**
- Depth First Search (DFS)
- Breadth First Search (BFS)

## DFS - Binary Trees
- In-Order
- Pre-Order
- Post-Order

### In-Order Traversal
- **Order**: Left -> Current -> Right
```python
def in_order_traversal(self, current_node):
    if current_node:
        self.in_order_traversal(current_node.left_child)
        print(current_node.data)
        self.in_order_traversal(current_node.right_child)
my_tree.in_order_traversal(my_tree.root)
```

- **Complexity**: $O(n)$
  - $n \rightarrow$ number of nodes

### Pre-Order Traversal
- **Order**: Current -> Left -> Right
```python
def pre_order_traversal(self, current_node):
    if current_node:
        print(current_node.data)
        self.pre_order_traversal(current_node.left_child)
        self.pre_order_traversal(current_node.right_child)
my_tree.pre_order_traversal(my_tree.root)
```

### Post-Order Traversal
- **Order**: Left -> Right -> Current
```python
def post_order_traversal(self, current_node):
    if current_node:
        self.post_order_traversal(current_node.left_child)
        self.post_order_traversal(current_node.right_child)
        print(current_node.data)
my_tree.post_order_traversal(my_tree.root)
```

### When to use In-Order, Pre-Order, and Post-Order Traversal
- **in-order**
  - used BST to obtain the node's values in ascending order
- **pre-order**
  - create copies of a tree
  - get prefix expressions
- **post-order**
  - delete binary trees
  - get postfix expressions

## DFS - Graphs
- Graphs can have cycles
  - need to keep track of visited vertices
- Steps:
  1. Start at any vertex
  2. Tracks current vertex to visited vertices list
  3. For each current node's adjacent vertex
    - If it has been visited $\rightarrow$ ignore it
    - If it hasn't been visited $\rightarrow$ recursively perform DFS

```python
def dfs(visited_vertices, graph, current_vertex):
    if current_vertex not in visited_vertices:
        print(current_vertex)
        visited_vertices.add(current_vertex)
        for adjacent_vertex in graph[current_vertex]:
            dfs(visited_vertices, graph, adjacent_vertex)
```

- **Complexity**: $O(V+E)$
  - $V \rightarrow$ number of vertices
  - $E \rightarrow$ number of edges

# Breadth First Search (BFS)

## Breadth First Search - Binary Trees
- Starts from the root
- Visits every node of every level

```python
def bfs(self):
    if self.root:
        visited_nodes = []
        bfs_queue = queue.SimpleQueue()
        bfs_queue.put(self.root)
        while not bfs_queue.empty():
            current_node = bfs_queue.get()
            visited_nodes.append(current_node.data)
            if current_node.left:
                bfs_queue.put(current_node.left)
            if current_node.right:
                bfs_queue.put(current_node.right)
        return visited_nodes
```

- **Complexity**: $O(n)$

## Breadth First Search - Graphs
- graphs can have cycles
  - Need to check if the node has been visited

```python
def bfs(graph, initial_vertex):
    visited_vertices = []
    bfs_queue = queue.SimpleQueue()
    bfs_queue.put(initial_vertex)
    while not bfs_queue.empty():
        current_vertex = bfs_queue.get()
        for adjacent_vertex in graph[current_vertex]:
            if adjacent_vertex not in visited_vertices:
                visited_vertices.append(adjacent_vertex)
                bfs_queue.put(adjacent_vertex)
    return visited_vertices
```

- **Complexity**: $O(V + E)$
  - V $ \rightarrow $ number of vertices
  - E $ \rightarrow $ number of edges

## BFS vs DFS

|BFS|DFS|
|--|--|
|Target **close** to the **starting vertex**| Target **far away** from the **starting vertex**|
|Applications:|Applications:|
|- Web crawler|- Solving puzzles with only one solutions (eg. mazes)|
|- Finding shortest path in unweighted graphs|Detecting cycles in graphs|
|- Finding connected locations using GPS|Finding shortest path in a weighted graph|
|-Used as part of other more complex algorithms|-Used as part of other more complex algorithms|

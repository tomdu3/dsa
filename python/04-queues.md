# Queues

- FIFO: First In First Out
  - **First inserted** item will be always the **first** item to be **removed**

## Queues - structure
- beginning: **head**
- end: **tail**
- **enqueue**: **can** only **add** at the **tail**
- **dequeue**: **can** only **remove** from the **head**

## Different types of queues
-  Doubly ended queues
-  Circular queues
-  Priority queues

## Queues - real uses
- printing tasks in a printer
  - documents are printed in the order they are received
- applications where the **order of requests matters**
  - tickets for a concert
  - taxi services

## Queues - implementation
- by using simple linked lists

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def dequeue(self):
        if self.head:
            current_node = self.head
            self.head = self.head.next
            current_node.next = None

            if self.head == None:
                self.tail = None
```

## SimpleQueue in Python
- module: **queue**
  - Queue
  - SimpleQueue

```python
import queue

orders_queue = queue.SimpleQueue()

orders_queue.put('Sushi')
orders_queue.put('Pizza')
orders_queue.put('Pasta')

print('The size is: ', orders_queue.qsize())

print(orders_queue.get())  # get the first inserted item and pops it
print(orders_queue.get())
print(orders_queue.get())

print('Empty queue: ', orders_queue.empty())
```


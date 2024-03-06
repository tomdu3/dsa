# Stacks


- LIFO: Last In First Out
    - **Last inserted** item will be always the **first** item to be **removed**
- Can only **add** at the **top**
  - _**Pushing** onto the stack_
- Can only **remove** from the **top**

![Stack representation](./docs/pictorial-representation-of-stack.png)

## Stack - real uses
- **Undo** feature in text editors:
  - **push** each keystroke
  - **pop** last inserted keystroke

- Symbol checker: ([{}]) - in programming
  - **push** opening symbol
  - **check** closing symbol
  - **pop** matching open symbol

- **Function calls** in programming
  - **push** block of memory
  - **pop** after the execution ends

## Stack - implementation
- by using singly linked lists

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        return popped_node.value
    
    def peek(self):
        if self.top:
            return self.top.value
        return None
```

- instead of creating stack from scratch, we can use the Python module **queue**
  - LifoQueue:
    - Python's *queue* module
    - behaves like a stack

```python
import queue

my_book_stack = queue.LifoQueue(maxsize=0)
my_book_stack.put("The Catcher in the Rye")
my_book_stack.put("To Kill a Mockingbird")
my_book_stack.put("Pride and Prejudice")

print('The size is: ', my_book_stack.qsize())
print(my_book_stack.get())  # get the first inserted item and pops it
print(my_book_stack.get())
print(my_book_stack.get())
print('Empty stack: ', my_book_stack.empty())
```

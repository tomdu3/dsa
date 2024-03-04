class Node:

    def __init__(self, data):
        self.value = data
        self.next = None

    def insert_at_beginning(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def remove_at_beginning(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next


class LinkedList:
    def ___init__(self):
        self.head = None
        self.tail = None



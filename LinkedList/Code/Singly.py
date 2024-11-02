class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class SLL:
    def __init__(self):
        self.head = None

    def addFirst(self, val):
        new_node = Node(val, self.head)
        self.head = new_node

    def addLast(self, val):
        if self.head is None:
            self.addFirst(val)
        else:
            root = self.head
            while root.next:
                root = root.next
            root.next = Node(val)

    def addParticular(self, pos, val):
        if pos <= 0:
            print('Position must be greater than 0')
            return
        if pos == 1:
            self.addFirst(val)
        else:
            root = self.head
            while pos > 2 and root and root.next:
                root = root.next
                pos -= 1
            if pos > 2 or not root:
                print('Index out of Bound Error')
            else:
                root.next = Node(val, root.next)

    def removeFirst(self):
        if self.head is not None:
            self.head = self.head.next
        else:
            print('No nodes found to remove.')

    def removeLast(self):
        if self.head is None:
            print('No nodes found to remove.')
            return
        if self.head.next is None:  # Single node case
            self.head = None
        else:
            root = self.head
            prev = None
            while root.next:
                prev = root
                root = root.next
            prev.next = None

    def removeParticular(self, val):
        if self.head is None:
            print('No nodes found to remove.')
            return
        if self.head.val == val:  # Remove first node if it matches `val`
            self.head = self.head.next
            return
        root = self.head
        prev = None
        while root:
            if root.val == val:
                prev.next = root.next
                return
            prev = root
            root = root.next
        print('Element not found.')

    def display(self):
        root = self.head
        while root:
            print(root.val, end=' -> ')
            root = root.next
        print('None')

# Testing the updated code
obj = SLL()
obj.addFirst(10)     
obj.addLast(11) 
obj.addLast(12) 
obj.addLast(13) 
obj.addParticular(6, 39)
obj.display()
obj.removeParticular(13)
obj.display()
obj.removeParticular(11)
obj.display()
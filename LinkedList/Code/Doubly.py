class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class DLL:
    def __init__(self):
        self.head = None

    def addFirst(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            root = self.head
            root.prev = Node(val, next=root)
            self.head = root.prev

    def addLast(self, val):
        if self.head is None:
            self.addFirst(val)
        else:
            root = self.head
            while root.next:
                root = root.next
            root.next = Node(val, prev=root)

    def addParticular(self, pos, val):
        if pos == 1 or self.head is None:
            self.addFirst(val)
        else: 
            root = self.head
            while pos > 1 and root:    
                pos -= 1
                root = root.next
            if pos == 1:
                temp = root.prev
                node = Node(val, root, temp)
                temp.next = node
                root.prev = node
            else:
                print("Cannot insert at that position")

    def removeFirst(self):
        if self.head is not None:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

    def removeLast(self):
        if self.head is not None:
            root = self.head
            while root.next:
                root = root.next
            if root.prev:
                root.prev.next = None
            else:
                self.head = None

    def removeParticular(self, val):
        if self.head is not None:
            root = self.head
            while root:
                if root.val == val:
                    if root.prev:
                        root.prev.next = root.next
                    else:
                        self.head = root.next
                    if root.next:
                        root.next.prev = root.prev
                    return
                root = root.next
            print("Not Found")

    def display(self):
        root = self.head
        while root:
            print(root.val, end=' -> ')
            root = root.next
        print('None')

# Example Usage
obj = DLL()
obj.addFirst(1)
obj.addLast(2)
obj.addLast(4)
obj.addLast(3)
obj.display()
obj.addParticular(1, 5)
obj.display()
obj.addParticular(2, 10)
obj.display()
obj.addParticular(4, 11)
obj.display()
obj.removeLast()
obj.removeParticular(10)
obj.display()

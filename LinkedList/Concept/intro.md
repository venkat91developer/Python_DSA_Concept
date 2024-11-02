### Linked List: Definition
A linked list is a linear data structure in which elements, called nodes, are stored in a sequence. Each node contains two parts:
- **Data:** The value of the node.
- **Pointer:** A reference to the next node in the sequence.

Unlike arrays, linked lists do not store elements in contiguous memory locations. Instead, each node points to the next, creating a chain-like structure.

### Types of Linked Lists
1. **Singly Linked List:** Each node points to the next node in the list. Traversal is one-way.
2. **Doubly Linked List:** Each node has two pointers: one pointing to the next node and one pointing to the previous node, allowing two-way traversal.
3. **Circular Linked List:** The last node points back to the first node, forming a circle. It can be singly or doubly linked.
4. **Circular Doubly Linked List:** Combines the features of both circular and doubly linked lists, where the last node points to the first, and each node has pointers to both the previous and next nodes.

### Characteristics of Linked Lists
- **Dynamic Size:** Nodes can be added or removed easily, unlike arrays with fixed sizes.
- **Efficient Insertions/Deletions:** Particularly in the middle or at the beginning, these operations do not require shifting elements as in arrays.
- **Sequential Access:** Nodes must be accessed sequentially from the head, as there is no index-based access.

### Why Linked Lists Are Needed
Linked lists are useful when:
- You need frequent insertions and deletions.
- Memory management is important, as linked lists are not contiguous.
- You require dynamic memory allocation without knowing the total number of items in advance.

### Advantages of Linked Lists
- **Dynamic Size:** The list can grow or shrink as needed.
- **Efficient Insertions and Deletions:** Adding or removing nodes at the beginning, middle, or end is efficient.
- **Memory Utilization:** Memory allocation is handled dynamically, which can save memory in some cases.

### Disadvantages of Linked Lists
- **No Direct Access:** Nodes must be accessed sequentially, leading to slower searches.
- **Extra Memory Use:** Each node requires extra memory for the pointer.
- **Complexity in Reverse Traversal:** Singly linked lists do not support direct backward traversal.

### Real-Time Examples of Linked Lists
- **Music Playlist:** Songs in a playlist where each song points to the next.
- **Image Viewer:** Allows moving back and forth between images.
- **Browser History:** Stores browsing history, allowing the user to go back and forth between visited pages.
- **Operating System Task Scheduling:** The OS scheduler maintains the processes/tasks using a linked list structure.

### Time Complexity of Operations
| Operation       | Singly Linked List | Doubly Linked List | Circular Linked List | Circular Doubly Linked List |
|-----------------|--------------------|---------------------|-----------------------|-----------------------------|
| Insertion (Head)| O(1)               | O(1)               | O(1)                  | O(1)                        |
| Insertion (Tail)| O(n)               | O(1)               | O(n)                  | O(1)                        |
| Deletion (Head) | O(1)               | O(1)               | O(1)                  | O(1)                        |
| Deletion (Tail) | O(n)               | O(n)               | O(n)                  | O(n)                        |
| Search          | O(n)               | O(n)               | O(n)                  | O(n)                        |
| Access by Index | O(n)               | O(n)               | O(n)                  | O(n)                        |

### Space Complexity
For all types of linked lists, the space complexity is **O(n)**, where **n** is the number of nodes in the list. Each node requires additional memory to store a pointer (or two pointers, in the case of doubly linked lists).
### **Space Complexity**:
Space complexity refers to the amount of memory (space) required by an algorithm to run to completion. This includes:

1. **Fixed Part**: 
   - Independent of the input size.
   - Memory required for constants, program variables, and instructions.

2. **Variable Part**: 
   - Depends on the input size.
   - Memory required for dynamically allocated memory, recursion stack space, etc.

### **Types of Space Complexity**:

1. **Constant Space Complexity (O(1)):**
   - The algorithm uses a fixed amount of memory regardless of input size.
   - Example: Swapping two numbers, checking if a number is even or odd.

2. **Logarithmic Space Complexity (O(log N)):**
   - The memory usage grows logarithmically with the input size.
   - Example: Recursive binary search.

3. **Linear Space Complexity (O(N)):**
   - Memory usage grows linearly with the input size.
   - Example: Storing elements of an input array, using an additional array.

4. **Quadratic Space Complexity (O(N²)):**
   - Memory usage grows quadratically with the input size.
   - Example: Storing a 2D matrix for graph representations (adjacency matrix).

5. **Exponential Space Complexity (O(2^N)):**
   - Memory usage grows exponentially with the input size.
   - Example: Recursive solutions for problems like the Tower of Hanoi.

### **Factors Affecting Space Complexity**:
1. **Input size**: Larger input may require more space for variables, arrays, or data structures.
2. **Auxiliary space**: Extra space or temporary space used by the algorithm.
3. **Recursive stack space**: Memory required for function call stacks in recursion.

Here are detailed examples for **Auxiliary Space**, **Input Size**, and **Recursive Stack Space**:

---

### **1. Auxiliary Space**:
Auxiliary space is the extra space or temporary space used by an algorithm during its execution, excluding the space taken by the input data.

#### **Example: Merge Sort**
In Merge Sort, apart from the input array, additional space is required to store the temporary subarrays.

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
```

**Auxiliary Space**: \(O(N)\) for the temporary arrays used in merging.

---

### **2. Input Size**:
The space taken directly by the input data structure or elements.

#### **Example: Linear Search**
In linear search, the space complexity depends solely on the size of the input array.

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

**Space Complexity**: 
- Input size: \(O(N)\) to store the array.
- Auxiliary space: \(O(1)\) (only a few variables like `i` and `target`).

---

### **3. Recursive Stack Space**:
In recursive algorithms, each function call adds a new frame to the call stack. This stack space depends on the depth of recursion.

#### **Example: Fibonacci Sequence (Recursive)**
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

**Recursive Stack Space**:  
- Each recursive call uses stack space. 
- For \(fibonacci(n)\), the recursion depth is \(O(N)\) (linear recursion stack for `n` levels).

#### **Example: Factorial Calculation (Recursive)**

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

**Recursive Stack Space**:  
For \(factorial(5)\), the recursion stack looks like this:
```
factorial(5)
factorial(4)
factorial(3)
factorial(2)
factorial(1)
```
Each level adds \(O(1)\) space, and the total stack space is \(O(N)\) for `N` levels of recursion.

---

**Auxiliary space** is considered when analyzing the additional memory used by an algorithm **besides the input data**. It includes temporary variables, data structures, recursion stack, etc., that the algorithm requires during execution.

### **When to Consider Auxiliary Space?**
1. **Temporary Data Structures**:
   - If the algorithm creates additional arrays, lists, hash maps, trees, or other data structures.
   - Example: Merging two sorted arrays.

2. **Recursive Calls**:
   - Each recursive call adds a new frame to the call stack, so recursive algorithms often have \(O(\text{depth of recursion})\) auxiliary space.
   - Example: Depth-First Search (DFS) in a tree or graph.

3. **Dynamic Programming (DP)**:
   - If a table is created for memoization or tabulation.
   - Example: Solving the Fibonacci sequence using bottom-up DP.

4. **Sorting Algorithms**:
   - Some sorting algorithms (like Merge Sort) use auxiliary arrays, leading to \(O(n)\) auxiliary space.

5. **Temporary Variables**:
   - If the algorithm uses additional pointers, counters, or other temporary variables.
   - Typically \(O(1)\) unless the number of temporary variables scales with input size.

### **Not Considered Auxiliary Space**:
- Space used to store the input itself is not counted as auxiliary space, only the extra memory required during processing.
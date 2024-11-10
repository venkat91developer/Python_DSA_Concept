### **Time Complexity**

**Time Complexity** refers to the amount of time an algorithm takes to run as a function of the size of its input. It helps in analyzing how the execution time increases as the input size grows.

### **Types of Time Complexity**

Time complexity can be classified into three major types based on the input scenario:

1. **Best Case**:
   - The time complexity for the most efficient case (optimal scenario).
   - Example: In linear search, finding the target at the first index results in \(O(1)\).

2. **Average Case**:
   - The expected time complexity when the input is random.
   - Example: In linear search, assuming the element is found halfway on average, the time complexity is \(O(N/2) \approx O(N)\).

3. **Worst Case**:
   - The time complexity in the least efficient scenario.
   - Example: In linear search, when the element is not present or at the last index, the time complexity is \(O(N)\).

---

### **Categories of Time Complexity**

1. **Constant Time Complexity (O(1)):**
   - The execution time does not depend on the input size.
   - Example: Accessing an element from an array.

   ```python
   def get_first_element(arr):
       return arr[0]
   ```

2. **Logarithmic Time Complexity (O(log N)):**
   - The execution time grows logarithmically as the input size increases.
   - Example: Binary Search.

   ```python
   def binary_search(arr, target):
       low, high = 0, len(arr) - 1
       while low <= high:
           mid = (low + high) // 2
           if arr[mid] == target:
               return mid
           elif arr[mid] < target:
               low = mid + 1
           else:
               high = mid - 1
       return -1
   ```

3. **Linear Time Complexity (O(N)):**
   - The execution time grows linearly with the input size.
   - Example: Linear Search.

   ```python
   def linear_search(arr, target):
       for i in range(len(arr)):
           if arr[i] == target:
               return i
       return -1
   ```

4. **Linearithmic Time Complexity (O(N log N)):**
   - The execution time grows in proportion to \(N \log N\).
   - Example: Merge Sort, Heap Sort.

5. **Quadratic Time Complexity (O(N²)):**
   - The execution time grows quadratically with the input size.
   - Example: Bubble Sort, Selection Sort.

   ```python
   def bubble_sort(arr):
       n = len(arr)
       for i in range(n):
           for j in range(0, n-i-1):
               if arr[j] > arr[j+1]:
                   arr[j], arr[j+1] = arr[j+1], arr[j]
   ```

6. **Cubic Time Complexity (O(N³)):**
   - The execution time grows cubically with the input size.
   - Example: Solving the matrix multiplication problem.

7. **Exponential Time Complexity (O(2^N)):**
   - The execution time doubles with each additional input element.
   - Example: Recursive Fibonacci.

   ```python
   def fibonacci(n):
       if n <= 1:
           return n
       return fibonacci(n - 1) + fibonacci(n - 2)
   ```

8. **Factorial Time Complexity (O(N!)):**
   - The execution time grows factorially with the input size.
   - Example: Solving the Traveling Salesman Problem (TSP) using brute force.

---

### **Common Time Complexities and Their Growth**

| **Time Complexity** | **Example**             | **Growth Rate**     |
|----------------------|--------------------------|----------------------|
| \(O(1)\)             | Accessing array element  | Constant             |
| \(O(\log N)\)        | Binary Search            | Logarithmic          |
| \(O(N)\)             | Linear Search            | Linear               |
| \(O(N \log N)\)      | Merge Sort               | Linearithmic         |
| \(O(N^2)\)           | Bubble Sort              | Quadratic            |
| \(O(N^3)\)           | Matrix Multiplication    | Cubic                |
| \(O(2^N)\)           | Recursive Fibonacci      | Exponential          |
| \(O(N!)\)            | Traveling Salesman (TSP) | Factorial            |

---
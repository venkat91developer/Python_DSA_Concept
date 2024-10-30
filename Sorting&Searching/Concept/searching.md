# SEARCHING ALGORITHM
## 1. LINEAR SEARCH
**Code**:
```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

**Time Complexity**:
- Best case: O(1) (when the target is the first element)
- Average case: O(n)
- Worst case: O(n) (when the target is not present or is at the last position)

**Real-time Usage**:
- Small datasets where the overhead of more complex algorithms is not justified.
- Unsorted arrays or lists where binary search can't be applied.
- Situations where the dataset is continuously changing, and sorting it is not efficient.

**Pros**:
- Simple to implement.
- Works on both sorted and unsorted arrays.
- No additional memory overhead.

**Cons**:
- Inefficient for large datasets due to O(n) time complexity.
- Not suitable for scenarios where fast search is required, especially for large arrays.

## 2. BINARY SEARCH
### Iterative Method:
**Code**
```python
def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### Recursive Method:
**Code**
```python
def binary_search_recursive(arr, target, left, right):
    if left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, right)
        else:
            return binary_search_recursive(arr, target, left, mid - 1)
    return -1
```

**Time Complexity**:
- Best case: O(1)
- Average case: O(log n)
- Worst case: O(log n)

**Real-time Usage**:
- Efficient searching in sorted arrays or lists.
- Frequently used in applications where a large dataset needs to be searched quickly, such as database lookups or dictionary operations.

**Pros**:
- Much faster than linear search for large datasets.
- Efficient with O(log n) time complexity.

**Cons**:
- Requires the array to be sorted.
- More complex to implement than linear search.


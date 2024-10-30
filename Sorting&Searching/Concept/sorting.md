# SORTING ALGORITHM
## 1. BUBBLE SORT

**Information:**
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The process is repeated until no swaps are needed, indicating that the list is sorted.

**Code:**
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

**Pros:**
- Simple to understand and implement.
- Easy to teach as an introductory algorithm.

**Cons:**
- Inefficient on large datasets (O(n²) complexity).
- Not suitable for large lists.

**Real-Time Usage:**
- Used in educational contexts to illustrate sorting concepts.
- Suitable for small datasets or nearly sorted data.

**Time Complexity:**
- Best Case: O(n)
- Average Case: O(n²)
- Worst Case: O(n²)

##  2. INSERTION SORT

**Information:**Insertion Sort builds the final sorted array one item at a time. It works similarly to the way you sort playing cards in your hands. It picks each element and places it in the correct position relative to the previously sorted elements.
**Code:**
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

**Pros:**
- Efficient for small datasets.
- Adaptive; performs well on partially sorted data.

**Cons:**
- Inefficient on large datasets (O(n²) complexity).
- Performance degrades significantly with larger lists.

**Real-Time Usage:**
- Useful for sorting small or partially sorted datasets.
- Often used in hybrid sorting algorithms (e.g., Timsort).

**Time Complexity:**
- Best Case: O(n)
- Average Case: O(n²)
- Worst Case: O(n²)

## 3. SELECTION SORT
**Information:**
Selection Sort divides the input list into two parts: the sorted part at the front and the unsorted part at the back. It repeatedly selects the smallest (or largest, depending on sorting order) element from the unsorted portion and moves it to the sorted portion.
**Code:**
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

**Pros:**
- Simple to implement.
- Performs well on small lists.

**Cons:**
- Inefficient on large datasets (O(n²) complexity).
- Not adaptive; does not take advantage of existing order in the array.

**Real-Time Usage:**
- Useful for small datasets or when memory space is a constraint.
- Suitable when the overhead of more complex algorithms is not justified.

**Time Complexity:**
- Best Case: O(n²)
- Average Case: O(n²)
- Worst Case: O(n²)

##  4. QUICK SORT
**Information:**
Quick Sort is a divide-and-conquer algorithm that sorts an array by selecting a 'pivot' element and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

**Code:**
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

**Pros:**
- Very efficient for large datasets.
- Average-case time complexity is O(n log n).
- In-place sorting (low space complexity).



**Cons:**
- Worst-case time complexity is O(n²) (rare, usually when the smallest or largest element is chosen as the pivot).
- Not a stable sort; relative order of equal elements may not be preserved.

**Real-Time Usage:**
- Widely used in various applications, including database and sorting libraries.
- Preferred in scenarios where average-case performance is essential.

**Time Complexity:**
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n²)

##  5. MERGE SORT
**Information:**
Merge Sort is another divide-and-conquer algorithm that splits the array into halves, sorts each half, and then merges the sorted halves back together. It is stable and guarantees O(n log n) performance regardless of the input.

**Code:**
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr
```

**Pros:**
- Stable sorting algorithm.
- Guaranteed O(n log n) time complexity in all cases.
- Suitable for linked lists and large datasets.

**Cons:**
- Requires additional space for merging (O(n) space complexity).
- More complex implementation compared to simpler algorithms.

**Real-Time Usage:**
- Used in sorting algorithms in various programming libraries (e.g., Python's `sorted()`).
- Effective for sorting large datasets and linked lists.

**Time Complexity:**
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)

##  6. BUCKET SORT
**Information:**
Bucket Sort distributes the elements of an array into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm or recursively applying the bucket sort. Finally, the sorted buckets are concatenated to form the final sorted array.

**Code:**
```python
def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    
    max_value = max(arr)
    size = max_value // len(arr) + 1
    buckets = [[] for _ in range(size)]

    for num in arr:
        index = num // len(arr)
        buckets[index].append(num)

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))
    
    return sorted_array
```


**Pros:**
- Efficient for uniformly distributed data.
- Can achieve linear time complexity O(n) under ideal conditions.

**Cons:**
- Performance depends on the distribution of the input data.
- Requires extra space for the buckets (O(n) space complexity).

**Real-Time Usage:**
- Used in applications that require sorting of floating-point numbers or uniformly distributed data.
- Suitable for external sorting algorithms.

**Time Complexity:**
- Best Case: O(n)
- Average Case: O(n + k) where k is the number of buckets.
- Worst Case: O(n²) if all elements fall into the same bucket.

class Sort:
    def __init__(self):
        pass
    def bubbleSort(self,a):
        n = len(a)
        for i in range(n):
            for j in range(0,n-i-1):
                if a[j]>a[j+1]:
                    a[j],a[j+1] = a[j+1],a[j]
        return a
    def selectionSort(self,a):
        n = len(a)
        for i in range(n):
            min_idx = i
            for j in range(i+1,n):
                if a[min_idx]>a[j]:
                    min_idx = j
            a[i],a[min_idx] = a[min_idx],a[i]
            print(a)
        return a
    def mergeSort(self,a):
        if len(a)<=1:
            return a
        mid = len(a)//2
        left = self.mergeSort(a[:mid])
        right = self.mergeSort(a[mid:])
        return self.merge_sort(left,right)
    def merge_sort(self,left,right):
        sorted_arr = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i]<right[j]:
                sorted_arr.append(left[i])
                i+=1
            else:
                sorted_arr.append(right[j])
                j+=1
        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        return sorted_arr
    def quickSort(self,a):
        if len(a)<=1:
            return a
        pivot = a[len(a)//2]
        left = [x for x in a if x<pivot]
        middle = [x for x in a if x==pivot]
        right = [x for x in a if x>pivot]
        return self.quickSort(left)+middle+self.quickSort(right)
obj = Sort()
a = [14,12,15,16,99,12,42,15,28,17,57]
#print('BUBBLE SORT: ',obj.bubbleSort(a))
#print('SELECTION SORT: ',obj.selectionSort(a))
#print('MERGE SORT: ',obj.mergeSort(a))
#print('QUICK SORT: ',obj.quickSort(a))
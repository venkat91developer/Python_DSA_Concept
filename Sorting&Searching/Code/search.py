class Search:
    def linearSearch(self,a,search):
        for i in range(len(a)):
            if a[i] == search:
                return i
        return -1
    def binarySearch(self,a,search):
        s,e = 0, len(a)-1
        
        while s<=e:
            mid = (s+e)//2
            if a[mid] == search:
                return mid
            elif a[mid]>search:
                e = mid-1
            else:
                s = mid+1
        return -1
obj = Search()
a = [1,2,3,4,5,6,7,8,9,10]
print('Linear Search: ',obj.linearSearch(a,4))
print('Binary Search: ',obj.binarySearch(a,4))

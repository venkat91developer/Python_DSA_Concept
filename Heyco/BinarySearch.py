from typing import List
class Binary:
    def ballWeightScale(self,n,target):
        s,e,step,isNotFound = 1,n,1,True
        while(s<=e):
            m = (s+e)//2
            if m == target:
                isNotFound = False
                print(step)
                break
            elif m>target:
                e = m-1
                step+=1
            else:
                s = m+1
                step+=1
        if (isNotFound):
            print('Not Found')
    def NearestSQRT(self,n):
        if n==0:
            print(0)
            return 
        s,e,res = 1,n,-1
        while(s<=e):
            m = (s+e)//2
            if m == n/m:
                res = m
                break 
            elif m>n/m:
                e = m-1
                res = m-1
            else:
                s = m+1
                res = m
        print(res)
    def findRoutedUniqueArray(self,nums,target):
        s,e = 0,len(nums)-1
        while(s<=e):
            m = (s+e)//2
            if(nums[m] == target):
                return m
            elif nums[s]<=nums[m]:
                if(nums[s]<=target<=nums[m]):
                    e = m-1
                else:
                    s=m+1
            else:
                if(nums[m]<=target<=nums[e]):
                    s = m+1
                else:
                    e=m-1
        return -1
    def findRouteDuplicateArray(self,nums,target):
        s,e = 0,len(nums)-1
        while(s<=e):
            m = (s+e)//2
            if nums[m]==target :
                return m
            if nums[s] == nums[m] == nums[e]:
                s+=1
                e-=1
            elif nums[s]<=nums[m]:
                if nums[s]<=target<=nums[m]:
                    e = m-1
                else:
                    s = m+1
            else:
                if nums[m]<=target<=nums[e]:
                    s = m+1
                else:
                    e = m-1
        return -1
    def lowerBound(self,a,k):
        s,e,ans = 0,len(a)-1,len(a)
        while(s<=e):
            m = (s+e)//2
            if a[m]>=k:
                ans = m
                e = m-1
            else:
                s = m+1
        return ans
    def upperBound(self,arr,n,x):
        s,e,ans = 0,n-1,n
        while(s<=e):
            m = (s+e)//2
            if(arr[m]>x):
                ans = m
                e = m-1
            else:
                s = m+1
        return ans
    def searchInsert(arr, m):
        low = 0
        high = len(arr)-1
        ans = high+1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= m:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1  
        return ans
    def floor(a,n,x):
        s,e,ans = 0,n-1,-1
        while(s<=e):
            m = (s+e)//2
            if(a[m]<=x):
                ans = m
                s = m+1
            else:
                e = m-1
        if ans == -1: 
            return -1
        return a[ans]
    def ceil(a,n,x):
        s,e,ans = 0,n-1,-1
        while(s<=e):
            m = (s+e)//2
            if(a[m]>=x):
                ans = m
                e = m-1
            else:
                s = m+1
        if ans == -1: 
            return -1
        return a[ans]
        return [floor(a,n,x),ceil(a,n,x)]
    def firstAndLastOccurance(self, nums, target):
        lb = self.lowerBound(nums,target)
        if(lb == len(nums) or nums[lb]!=target):
            return [-1,-1]
        up = self.upperBound(nums,len(nums),target)
        return [lb,up-1]
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)-1
        if n==0:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[n] > nums[n-1]:
            return n
        s,e = 1,n-1
        while(s<=e):
            m = (s+e)//2
            if nums[m-1]<nums[m]>nums[m+1]:
                return m
            elif nums[m]>nums[m-1]:
                s = m+1
            else:
                e = m-1
        return -1
obj = Binary()
# arr = [4, 5, 6, 7, 0, 1, 2]
# target = 0

obj.ballWeightScale(100,3)
# obj.NearestSQRT(7)
# print(obj.findRoutedArray(arr,target))
# a = [3, 5, 8, 15, 19]
# n = 5
# k = 5
# print(obj.lowerBound(a,k))
# print(obj.upperBound(a,n,k))


#Q1: Function: ballWeightScale()
# Consider you have 100 balls which look the same but one out of them is either heavier or lighter than the rest . You are given a beam balance , then find out in minimum how many steps can you determine which ball is the odd one out?

#Q2: Function: NearestSQRT()
#Finding nearest integer to the square root of a positive integer

#Q3: Function: findRoutedUniqueArray()
#Given a sorted and rotated array arr[] of n distinct elements, the task is to find the index of given target element in the array. If target is not present in the array, return -1.

#NOTES: Identify the Sorted Part
#1. Condition
    #a) a[m]==target
    #a) TRUE: a[s]<a[m] => if True Left Sorted: 
        #Check a[s]<=target<=a[m+1] TRUE: Elimate Right
    #b) FALSE: 
        #Check a[m]<=target<=a[e] TRUE: Elimate Left

#Q4: Function: findRouteDuplicateArray()
#Given a sorted and rotated array arr[] of n duplicte elements, the task is to find the index of given target element in the array. If target is not present in the array, return -1.

#NOTES: Trim Duplicate and Identify the Sorted Part
#1. Condition
    #a) a[m]==target
    #b) Elimnate  nums[s] == nums[m] == nums[e] - Trim() Array Then Continue Code
    #c) TRUE: a[s]<a[m] => if True Left Sorted: 
        #Check a[s]<=target<=a[m+1] TRUE: Elimate Right
    #d) FALSE: 
        #Check a[m]<=target<=a[e] TRUE: Elimate Left

#Q5: Function : lowerBound()
#Condition:
#1. Smallest Index 
#2. Sorted and Duplicate Element -> a[i]>=k

#Q6: Function : upperBound()
#Condition:
#1. Smallest Index 
#2. Sorted and Duplicate Element -> a[i]>k

#Q7: Function : searchInsert()
# Problem statement
# You are given a sorted array 'arr' of distinct values and a target value 'm'. You need to search for the index of the target value in the array.
# Note:
# 1. If the value is present in the array, return its index.
# 2. If the value is absent, determine the index where it would be inserted in the array while maintaining the sorted order. 
# 3. The given array has distinct integers.
# 4. The given array may be empty.

#Q8 & Q9: Function: floor() and ceil()
# Floor [FORMULA: a[m]<=x] of 'x' is the largest element in the array which is smaller than or equal to 'x'. 
# Ceiling [FORMULA: a[m]>=x] of 'x' is the smallest element in the array greater than or equal to 'x'. [Use Lower Bound]

#Q10: firstAndLastOccurance()
#Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

#Q11: Peak Element in Array
#FORMULA: a[i-1] < a[i] > a[i+1]
# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
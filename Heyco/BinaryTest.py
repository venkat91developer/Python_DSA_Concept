class Binary:
    def __init__(self,method):
        self.method = method
    def findBallWeight(self,n,target):
        if (self.method == 1):
            '''
            Approch 1: Navie Method or Brute Force Method
            Time Complexity:  O(n)
            Space Complexity: O(1)
            '''
            for i in range(1,n):
                if i == target:
                    return i
            return -1
        elif (self.method == 2):
            '''
            Approch 1: Navie Method or Brute Force Method
            Time Complexity:  O(log n)
            Space Complexity: O(1)
            ''' 
            s,e,counter = 1,n,0
            while s<=e:
                counter+=1
                m = (s+e)//2
                if m== target:
                    return counter
                elif m<target:
                    s = m+1 
                else:
                    e = m-1
            return -1
                
navie  = Binary(1)
better = Binary(2)
print('Naive Approach: ',navie.findBallWeight(100000,33334))
print('Better Approach: ',better.findBallWeight(100000,33334))
'''
Naive Approach:  33334 (TOO SLOWER)
Better Approach:  17 (MORE FASTER)
'''
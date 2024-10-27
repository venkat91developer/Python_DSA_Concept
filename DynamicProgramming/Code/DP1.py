class DP1:
    def __init__(self):
        pass
    #NORMAL RECURSIVE METHOD
    def fib(self,n):
        if n<=1:
            return n
        return self.fib(n-1)+self.fib(n-2)
    #MOMOIZATION METHOD
    def fibMemo(self,n,dp):
        if n <= 1:  # Base case
            return n
        if dp[n] == -1:
            dp[n] = self.fibMemo(n-1,dp)+self.fibMemo(n-2,dp)
        return dp[n]
        '''
        Time  Complexity: O(n)
        Space Complexity: O(n)
        '''
    #TABULATION METHOD
    def fibTab(self,n):
        dp = [-1] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for n in range(2,n+1):
            dp[n] = dp[n-1]+dp[n-2]
        return dp[n]
        '''
        Time  Complexity: O(n)
        Space Complexity: O(n)
        '''
    #TABULATION METHOD - SPACE OPTIMAL METHOD
    def fibTabOptimial(self,n):
        prev0 = 0
        prev1 = 1
        for n in range(1,n+1):
            curr = prev0+prev1
            prev1 = prev0
            prev0 = curr
        return prev0
        '''
        Time  Complexity: O(n)
        Space Complexity: O(1)
        '''

        
#FIBONNIC SERIES:
obj = DP1()
n = int(input('Enter the Fib Value (Greater than 0):'))
dp = [-1] * (n+1)
dp[0] = 0
dp[1] = 1
# print('Fibonnic Series:',obj.fibMemo(n,dp))
# print('Fibonnic List:',dp[:n-1])
# print('Fibonnic Series:',obj.fibTab(n))
print('Fibonnic Series:',obj.fibTabOptimial(n))

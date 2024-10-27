# Dynamic Programming (DP)

Dynamic Programming (DP) is a powerful technique used to solve complex problems by breaking them down into simpler subproblems. 

### It involves two main principles:

#### Optimal Substructure: 
A problem has an optimal substructure if an optimal solution to the problem contains optimal solutions to its subproblems.

#### Overlapping Subproblems: 
The problem has overlapping subproblems if the solution to the problem can be stored and reused multiple times.

### DP solutions are generally built in two ways:

#### Top-Down (Memoization): 
Start with the original problem, break it down, and store the solutions to subproblems to avoid redundant calculations.

#### Bottom-Up (Tabulation): 
Solve all possible subproblems first, storing each result in a table or array, and use these to solve the larger problem.

Common applications of DP include problems involving optimization, like **finding the longest subsequence, shortest path, or maximum sum in a sequence.** DP is widely used in combinatorial problems and optimization tasks.

To convert a recursive Fibonacci solution to use memoization (dynamic programming), you can follow these steps:

### Steps to Convert Recursive Fibonacci to Memoized DP

1. **Write the Basic Recursive Function**:
   ```py
   def fib(n):
       if n <= 1:
           return n
       return fib(n-1) + fib(n-2)
   ```

Here's the updated code with memoization:

```py
    dp = [-1] * n
    def fib(n):
        if n <= 1:
            return n
        if dp[n]==-1:
            dp[n] = fib(n-1) + fib(n-2)
        return dp[n]
```

### Explanation
**Step 1:** Declare DP Array with -1.
**Step 2:** Check DP[n] should be -1 then call recursive.
**Step 3:** If not -1 then return stored value.


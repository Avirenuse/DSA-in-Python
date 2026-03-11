# Dynamic Programming (DP)
# An algorithmic technique for solving an optimization problem by breaking it down into simpler subproblems
# and utilizing the fact that the optimal solution to the overall problem depends upon the optimal solution to its subproblems.

print("=== 1. Fibonacci Sequence (Memoization vs Tabulation) ===")

# Top-Down (Memoization)
# Time: O(n), Space: O(n)
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
        
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# Bottom-Up (Tabulation)
# Time: O(n), Space: O(n)
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(f"Fibonacci(10) using Memoization: {fib_memo(10)}")
print(f"Fibonacci(10) using Tabulation: {fib_tab(10)}")

print("\n=== 2. 0/1 Knapsack Problem ===")
# Given weights and values of n items, put these items in a knapsack of capacity W 
# to get the maximum total value in the knapsack.

# Bottom-Up Dynamic Programming
# Time: O(N * W), Space: O(N * W) where N is number of items and W is capacity
def knapsack(W, weights, values, n):
    # Base case matrix, initialized to 0
    # dp[i][w] will store the max value that can be attained with subset of first i items and max weight w
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # Build table dp[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                # Max of (including the item OR not including the item)
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                # Cannot include the item
                dp[i][w] = dp[i-1][w]
                
    return dp[n][W]

values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
n = len(values)

print(f"Max Knapsack Value (Capacity={W}):", knapsack(W, weights, values, n))

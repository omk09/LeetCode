# https://leetcode.com/problems/min-cost-climbing-stairs/solution/


# Buttom Up - Slowly Build a solution - Tabulation

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = [0]*(len(cost)+1)

        for i in range(2,len(cost)+1):
            minCost[i] = min(minCost[i-1]+cost[i-1], minCost[i-2]+cost[i-2])            
            
        return minCost[-1]



# Top-Down Dynamic Programming (Recursion + Memoization)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def recursiveMinCost(i):
            if i <= 1:
                return 0
            if i in memo:
                return memo[i]

            memo[i] = min(cost[i-1]+recursiveMinCost(i-1) , cost[i-2]+recursiveMinCost(i-2)) 
            return memo[i]
        
        
        memo = {}
        return recursiveMinCost(len(cost))

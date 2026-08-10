from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)

        @cache

        def minCost(i):

            if i >= n:

                return 0

            return cost[i] + min(minCost(i+1), minCost(i+2))

        return min(minCost(0), minCost(1))

 

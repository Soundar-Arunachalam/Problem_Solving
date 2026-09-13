class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def dfs(n):
            if n == 0:
                return cost[0]
            if n == 1:
                return cost[1]
            if n in cache:
                return cache[n]
            cache[n] =  min(dfs(n-1), dfs(n-2))+ (cost[n] if n < len(cost) else 0)
            return cache[n]
        n = len(cost)
        ans = dfs(n)
        return ans
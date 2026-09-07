# time complexity : O(N*M)
# space complexity : O(N)
# where N = amount and M = number of coins
class CoinChange:
    def coinChange(self, coins: list[int], amount: int) -> int:
        coins.sort()
        n = amount
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for j in coins:
                if i-j<0:
                    break
                if dp[i-j] != float('inf'):
                    dp[i] = min(dp[i], 1+dp[i-j])
        return dp[n] if dp[n] != float('inf') else -1
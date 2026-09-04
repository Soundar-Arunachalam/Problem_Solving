#technique: State machine DP
# time complexity : O(N)
# space complexity : O(1)
class Best_time_to_buy_and_sell_stock_with_cooldown:
    def maxProfit(self, prices):
        n = len(prices)

        if n <= 1:
            return 0

        s0 =  n
        s1 =  n
        s2 =  n

        s1 = -prices[0]
        s0 = 0
        s2 = float('-inf')

        for i in range(1, n):
            new_s0 = max(s0, s2)
            new_s1 = max(s1, s0 - prices[i])
            new_s2 = s1 + prices[i]
            s0 = new_s0
            s1 = new_s1
            s2 = new_s2

        return max(s0, s2)
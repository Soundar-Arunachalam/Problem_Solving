class Solution:
    def minCost(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return max(nums)

        # dp[i][j]:
        # nums[i] is the survivor
        # j is the next unseen index
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        # Base cases
        # j >= n -> only nums[i] remains
        for i in range(n):
            dp[i][n] = nums[i]

        # j == n-1 -> nums[i] and nums[n-1] remain
        for i in range(n - 1):
            dp[i][n - 1] = max(nums[i], nums[n - 1])

        # j goes backwards
        for j in range(n - 2, 1, -1):

            a = nums[j]
            b = nums[j + 1]

            for i in range(j):
                x = nums[i]

                dp[i][j] = min(
                    # Remove j and j+1
                    # i survives
                    max(a, b) + dp[i][j + 2],

                    # Remove i and j+1
                    # j survives
                    max(x, b) + dp[j][j + 2],

                    # Remove i and j
                    # j+1 survives
                    max(x, a) + dp[j + 1][j + 2]
                )

        return min(
            max(nums[0], nums[1]) + dp[2][3],
            max(nums[0], nums[2]) + dp[1][3],
            max(nums[1], nums[2]) + dp[0][3]
        )
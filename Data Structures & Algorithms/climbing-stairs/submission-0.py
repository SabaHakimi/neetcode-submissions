class Solution:
    def climbStairs(self, n: int) -> int:
        # int n -> num steps to reach top of staircase
        # can climb 1 or 2 steps at a time

        # return num distinct ways to climb to top
        # incremental value, can calc step by step
        # dp problem
        # need to find num permutations of steps to get to nth step
        #
        # n = 1 -> 1
        # n = 2 -> 1 + 1 or 2
        # n = 3 -> 1 + 1 + 1 or 1 + 2 or 2 + 1
        # n = 4 -> 1 + 1 + 1 + 1 or 1 + 2 + 1 or 2 + 1 + 1 or 1 + 1 + 2 or 2 + 2

        # key intution is for the nth step, you can either take one step from any of the combinations for the (n - 1)th step
        #                                              or take two steps from any of the combinations for the (n - 2)th step
        # so for nth step, the number of distinct ways to get there = dp[n - 1] + dp[n - 2]
        dp = [1, 2] # permutations to nth step
        if n == 1:
            return dp[0]
        if n == 2:
            return dp[1]

        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])

        return dp[-1]

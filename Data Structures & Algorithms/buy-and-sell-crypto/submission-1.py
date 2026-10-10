class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # expand right until you find a smaller value than current left bound,
        # at which point that becomes the new left bound
        # this is because any value the old bound could profit going forward, the new one will profit more
        l = 0
        r = 0
        max_profit = 0

        while r < len(prices):
            # Consider current
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)

            # Expand window
            r += 1
            if r < len(prices) and prices[r] < prices[l]:
                l = r

        return max_profit




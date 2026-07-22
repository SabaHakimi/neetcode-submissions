class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find the greatest difference in the array between
        # any value and a value following it
        # sliding window
        # update left bound when new smallest value found
        if len(prices) == 1:
            return 0

        max_profit = 0
        current_smallest = prices[0]
        r = 1

        while r < len(prices):
            if prices[r] < current_smallest:
                current_smallest = prices[r]
            elif prices[r] - current_smallest > max_profit:
                max_profit = prices[r] - current_smallest
            r += 1

        return max_profit
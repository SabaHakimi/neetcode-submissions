class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort(reverse=True)
        memo = {}
        return self.leastCoins(coins, amount, memo)

    def leastCoins(self, coins: List[int], amount: int, memo) -> int:
        best = float('inf')
        for i in range(len(coins)):
            diff = amount - coins[i]
            if diff == 0:
                return 1
            if diff > 0:
                if diff not in memo:
                    out = self.leastCoins(coins, diff, memo)
                    memo[diff] = out
                else:
                    out = memo[diff]
                if out != -1: 
                    best = min(best, out)
        if best == float('inf'):
            return -1
        return best + 1
        
        
        # [ 2, 5, 9] -> 15

        # [9, 5, 2] -> 15 -> 6 -> 1

        # brute force solution -> iterate list backwards trying coin combinations;
        # idea is fulfill with largest coins possible so you try to find the first combo
        # in the set of all existing combos that outputs the desired value

        


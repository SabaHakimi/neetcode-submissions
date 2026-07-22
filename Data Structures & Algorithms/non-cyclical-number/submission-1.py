class Solution:
    def isHappy(self, n: int) -> bool:
        # Recurse
        # Modulus parsing most likely
        # Write sum of squares helper
        # two pointers, fast and slow
        # 25 -> 4 + 25 = 29
        fast = n
        slow = n
        while fast != 1 and slow != 1:
            fast = self.getSumOfSquares(self.getSumOfSquares(fast))
            slow = self.getSumOfSquares(slow)
            if fast != 1 and fast == slow:
                return False
        return True


    def getSumOfSquares(self, n: int) -> int:
        sum = 0
        while n != 0:
            sum += (n % 10) ** 2
            n = n // 10
        return sum


    # 101
    # fast -> 101 -> 4 -> 37 -> 89 -> 42 -> 4  -> 37 -> 89  -> 42
    # slow -> 101 -> 2 -> 4  -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 
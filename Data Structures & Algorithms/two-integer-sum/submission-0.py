class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_bank = {}
        i = 0
        for num in nums:
            if (target - num) in num_bank:
                return [
                    min(i, num_bank[(target - num)]), 
                    max(i, num_bank[(target - num)])]
            num_bank[num] = i
            i += 1


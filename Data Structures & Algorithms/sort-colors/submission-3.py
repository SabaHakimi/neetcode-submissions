class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Base case
        if len(nums) == 1:
            return

        # Init ptrs
        nxt_zero = 0
        nxt_two = len(nums) - 1
        i = 0

        while i <= nxt_two:
            if nums[i] == 0:
                # Swap
                temp = nums[nxt_zero] 
                nums[nxt_zero] = nums[i]
                nums[i] = temp

                # Inc ptrs
                nxt_zero += 1
            elif nums[i] == 2:
                # Swap
                temp = nums[nxt_two] 
                nums[nxt_two] = nums[i]
                nums[i] = temp

                # Inc ptr
                nxt_two -= 1
                continue
            i += 1


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # track value up to a point from both left and right and mult by each other
        # is there a cleaner way to adjust these for simpler computation? yes
        # for both prefix and postfix: compute all values up until that point, not including current
        # default is 1 because of multiplication (left and right index edge cases)
        # this allows for directly multiplying prefix and postfix indices for solution values
        
        # calc prefixes
        prefix = [1] * len(nums)
        prefix[1] = nums[0]
        for i in range(2, len(nums)):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        
        # calc postfixes
        postfix = [1] * len(nums)
        postfix[-2] = nums[-1]
        for i in range(len(nums) - 3, -1, -1):
            postfix[i] = nums[i + 1] * postfix[i + 1]

        # calc output
        output = [0] * len(nums)
        for i in range(len(nums)):
            output[i] = prefix[i] * postfix[i]

        return output

        # input
        # [1, 2, 4, 6]

        # prefix
        # [1, 1, 2, 8]

        # postfix
        # [48, 24, 6, 1]

        # output
        # [48, 24, 12, 8]
class Solution:
    def rob(self, nums: List[int]) -> int:
        # input is array of neighboring houses (sorted positionally basically)
        # nums[i] reps amt of money ith house has

        # return max amt of money u can rob without alerting police
        
        # working towards a maximum
        # consider just one element in the array and get the max
        # then consider two
        # then three
        # dp problem
        
        # [1, 1, 3, 3]
        # 1 -> 1
        # 1, 1 -> 1
        # 1, 1, 3 -> 4
        # 1, 1, 3, 3 -> 4

        # cover base cases, then
        # for each newly introduced element:
        #   consider the max amount of money u can rob when only considering up to previous house and only up to the one before that
        #   for this house, max is either only up to prev or the value of current + only up to before prev
        
        # Base case
        first = nums[0]        
        if len(nums) == 1:
            return first
        
        second = max(nums[0], nums[1])
        if len(nums) == 2:
            return second

        # Get max
        nth_max = [first, second]
        
        for i in range(2, len(nums)):
            nth_max.append(max(nth_max[i - 1], nth_max[i - 2] + nums[i]))

        return nth_max[-1]
        
class Solution:
    def trap(self, height: List[int]) -> int:

        # need info from both left and right
        # not just immediate left and right but whole array
        # for each index in array:
        # what is the highest point that is ABOVE me to my left and to my right?
        # at this index, i can hold as much water as the difference from the lower of those two and i's height

        #solution:
        # build prefix and postfix arrays with 'max height to this point'
        # then just iterate array

        # build prefix
        prefix = [0] * len(height)
        max = 0
        for i in range(1, len(height)):
            if height[i - 1] > max:
                max = height[i - 1]
            prefix[i] = max

        # build postfix
        postfix = [0] * len(height)
        max = 0
        for i in range(len(height) - 2, -1, -1):
            if height[i + 1] > max:
                max = height[i + 1]
            postfix[i] = max

        # build output
        max_water = 0
        for i in range(len(height)):
            lower_bar = min(prefix[i], postfix[i])
            if lower_bar > height[i]:
                max_water += lower_bar - height[i]
        
        return max_water

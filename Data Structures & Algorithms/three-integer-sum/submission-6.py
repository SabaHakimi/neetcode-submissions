class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        threeSums = []

        for i in range(len(nums) - 1):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Init
            p1 = i + 1
            p2 = len(nums) - 1

            # Find pairs
            while p2 > p1:
                sum = nums[p1] + nums[p2] + nums[i]
                if sum == 0:
                    threeSums.append([nums[i], nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1
                    while p2 > p1 and nums[p1] == nums[p1 - 1]:
                        p1 += 1
                    while p2 > p1 and nums[p2] == nums[p2 + 1]:
                        p2 -= 1
                elif sum > 0:
                    p2 -= 1
                elif sum < 0:
                    p1 += 1

        return threeSums


        
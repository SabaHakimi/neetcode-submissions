class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # ascending, rotated
        # bin search almost certainly
        # 2 sorted halves
        # don't know where the split is or what the min/largest are
        # possible to know which direction, though
        # one half will always be sorted
        # if not sorted, it's possible there is a decreasing value between the left bound and right bound
        # always check which side sorted and see if it would exist within those bounds
        # else reduce search space to the other half
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                # this half sorted
                if nums[l] <= target and target <= nums[mid]:
                    # search this half
                    r = mid - 1
                else:
                    # search the other half
                    l = mid + 1
            elif nums[mid] <= nums[r]:
                # this half sorted
                if nums[mid] <= target and target <= nums[r]:
                    # search this half
                    l = mid + 1
                else:
                    # search the other half
                    r = mid - 1
            else:
                return -1
        
        return -1



import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # get max element in window at each step
        # O(nlogn) time, O(n) space
        # heap/priority queue -> NO
        # each time the window slides, need to figure out:
        # what is the new max?
        # did old max get phased out? new max phase in? or same max value
        # track a 'current_max" var
  

        # when the max gets phased out, how are you determining which of the elements in the window is the new max?
        # need a hierarchy?
        # neet to know at any point what the maximum value is not including previous value?
        # we care about the max in the window rather than the values of the list itself
        # track window vals somehow?
        # care about:
        #   hierarchy order of how big the value is *** cannot be recomputing max value
        #   index of the item
        # need to be able to access/update by index
        # if we somehow keep records of the max to a point, we can just say yes/no based on index out of bounds
        # i think solution is::
        # priority queue to determine current max, sorted by value, then by index
        # while index of top item is not valid at each step, pop
        # this forces out of bounds items to get popped, and will present items in order of max value.
        # nothing of value is ever discarded and a valid max item in the window will not be skipped 

        # solution:
        max_heap = []
        max_each_step = []

        l = 0
        r = -1
        
        # Slide window
        while r < len(nums):
            # at each step:
            # get max for current window
            # slide window
            if r - l + 1 == k:
                # Pop expired elements
                while max_heap[0][1] < l:
                    heapq.heappop(max_heap)
                max_each_step.append(-1 * max_heap[0][0])

            # Slide window
                l += 1
            
            r += 1
            if r < len(nums):
                heapq.heappush(max_heap, (-1 * nums[r], r))

        return max_each_step



        # 1 2 [1 0 4]  | k = 3

        # max_heap = [   (-1, 2) (0, 3)]
        # max_each_step = [2, 2]
        # l = 2
        # r = 4

        

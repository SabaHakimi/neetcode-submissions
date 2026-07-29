import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # always looking specifically for k'th largest
        self.heap_capacity = k
        self.min_heap = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # If heap is at capacity and val is greater than smallest item (top of min heap), pop it 
        if len(self.min_heap) == self.heap_capacity and self.min_heap[0] < val:
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, val)
        # If not at capacity, just push
        elif len(self.min_heap) < self.heap_capacity:
            heapq.heappush(self.min_heap, val)
        
        # Return k largest item in stream
        return self.min_heap[0]
        

    # want O(mlogk) time and O(k) space; m is num times add is called and k is rank of largest number to be tracked


    #  8 9 2 1 0 7 3 | 8 ; k = 4

    #  hc = 4
    #  m_h = [1, 9, 2, 8]


    

     # we don't really care about the stream at all.
     # we just want to keep track of the top k values
     # just want a min heap with these values of size k. if the top value is smaller than newly added value, pop and replace
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # list of weights
        # until one or 0 stone left:
        #   pick two heaviest
        #   if x == y:
        #   destroy both
        #   else:
        #       if x < y, x is destroyed and y has new weight x - y

        # biggest issue here is stones are not sorted, and we want to get the 2 heaviest each time
        # because we are smashing stones, and changing values, we cannot just sort once
        # heaps are good for situations where you need top k and are updating values

        # can do that in O(nlogn) time and O(n) space

        # Populate heap
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -1 * stone)

        # Smash stones until one or 0 remaining
        while len(max_heap) > 1:
            x = -1 * heapq.heappop(max_heap)
            y = -1 * heapq.heappop(max_heap)
            
            if x > y:
                x -= y
                heapq.heappush(max_heap, -1 * x)

        if max_heap:
            return -1 * max_heap[0]
        else:
            return 0

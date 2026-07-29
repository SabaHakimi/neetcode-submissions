import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # k closest sounds like a heap problem. let's see
        # for each element in the array get euclidean distance to origin to transform into usable value
        # then we just want k closest points; in any order

        # Build a max heap of size k
        # Add first k elements as distance, index pairs (for later retrieval)
        # Then, for each element
        # if distance is lower than max in max heap, pop max and add new element
        # else ignore it and go to next element
        max_heap = []
        output = []

        # Populate heap to capacity
        for i in range(k):
            euclidean_dist_to_origin = math.sqrt(points[i][0] ** 2 + points[i][1] ** 2)
            # Largest distance * -1 will be at top of heap
            heapq.heappush(max_heap, (-1 * euclidean_dist_to_origin, i))

        # Process remainder of points arr
        for i in range(k, len(points)):
            euclidean_dist_to_origin = math.sqrt(points[i][0] ** 2 + points[i][1] ** 2)
            # If dist is lower than max distance currently in heap, replace
            if euclidean_dist_to_origin < -1 * max_heap[0][0]:
                heapq.heapreplace(max_heap, (-1 * euclidean_dist_to_origin, i))
        
        # Return k closest points
        while len(max_heap) > 0:
            index = heapq.heappop(max_heap)[1]
            output.append(points[index])

        return output
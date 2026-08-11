import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sounds like a heap problem
        # unsorted array
        # aim for O(nlogk) time and O(k) space
        # log k hints towards heap of size k; pushing and popping n times
        # same with O(k) space
        # i think solution is to iterate list and track a heap of size k and at the end return
        # want min heap where you replace if current elmt greater than smallest element in heap
        # this will track top k elements and provide O(1) access to kth biggest

        topK = []

        # Iterate list
        for num in nums:
            # If heap not at capacity yet
            if len(topK) < k: 
                heapq.heappush(topK, num)
            
            # If num is greater than smallest element in heap, replace it
            elif num > topK[0]:
                heapq.heapreplace(topK, num)
            
        return topK[0]
            
        # [2, 3, 1, 5, 4], k = 2

        # topK = [4, 5]

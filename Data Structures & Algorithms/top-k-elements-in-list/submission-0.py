class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        topK = []

        # populate freqs dict
        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1
        
        # populate freq buckets
        for num, freq in freqs.items():
            buckets[freq].append(num)

        # return k most frequent
        i = len(buckets) - 1
        while len(topK) < k:
            for num in buckets[i]:
                topK.append(num)
            i -= 1
        
        return topK
        # store freqs in a dict
        # put freqs in buckets array length of nums
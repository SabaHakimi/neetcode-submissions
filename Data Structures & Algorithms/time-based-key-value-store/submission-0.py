class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # easily O(1) w/ append, timestamps strictly increase and no removals so will be sorted for get
        if key in self.store:
            self.store[key].append((timestamp, value))
        else:
            self.store[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        # retrieve key set with largest timestamp <= arg ts
        # O(logn) time, O(m * n) space, m keys n vals 
        # store list of value, timestamp pairs per key
        # bin search on timestamp to return value
        if key in self.store:
            vals = self.store[key]
            l = 0
            r = len(vals) - 1
            best = -1
            while l <= r: 
                mid = (l + r) // 2

                if vals[mid][0] == timestamp:
                    return vals[mid][1]

                if vals[mid][0] < timestamp:
                    if best == -1 or vals[mid][0] > vals[best][0]:
                        best = mid
                    l = mid + 1
                else:
                    r = mid - 1
     
            if best != -1:
                return vals[best][1]

        return ""

        # {
        #     "alice": [(1, "meow"), (2, "burp"), (3, "alligator")]
        # }

        # vals = [(1, "meow"), (2, "burp"), (3, "alligator")] get 3
        # l = 2
        # r = 2
        # best = 2
        # mid = 2
        # don't assume key exists or value exists


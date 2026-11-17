import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # list of tasks E {A-Z}
        # 1 cycle allows 1 task to be completed
        # identical tasks must be separated by at least n CPU cycles
        # return min num cycles required to complete all tasks
        # min cycles is between len(tasks) and len(tasks) * n + 1

        # want to optimize for fewest empty cpu cycles

        # to get minimum, cannot just iterate in order. need to know ahead of time whats in list of tasks

        # iterate list to create freq list for tasks
        # from there maybe answer can be mathematically derived but doesn't change big O complexity to just simulate task completion
        # want some kind of queue that pulls from a sorted freq list and requeues after n cycles
        # maybe queue up to n tasks at a time
        # then re-evaluate this sorted freq list

        # maybe use heap

        # get freq list
        # push all items to heap
        # then until all tasks completed (keep a counter):
        #   pop up to n items from heap, increment counter same num times
        #   readd to heap

        # build freq list
        freq_list = {}
        for task in tasks:
            if task in freq_list:
                freq_list[task] += 1
            else:
                freq_list[task] = 1

        # push list to heap
        heap = []
        for key in freq_list:
            heapq.heappush(heap, (freq_list[key] * -1, key))

        # run tasks
        count = 0
        while heap:
            popped = []
            i = 0

            # pop up to n items
            while i < n + 1:
                if heap:
                    task = heapq.heappop(heap)
                    new_freq = task[0] + 1
                    task = (new_freq, task[1])
                    if task[0] < 0:
                        popped.append(task)
                elif not popped:
                    return count
                count += 1
                i += 1

            # re-queue
            for task in popped:
                heapq.heappush(heap, task)
        
        return count
            
        heap = [(-2, x), (-2, y)]
        popped = [(-1, x), (-1, x)]
        count = 2

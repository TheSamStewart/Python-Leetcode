from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        While loop that only keeps track of time ONLY
        count frequency of all tasks - label does not matter
        we want to prioritise the most frequent task - max heap 
        when a task has been executed - add to back of deque with time when ready to be released back to max heap
        '''
        
        # If cooling interval is zero we can execute all tasks consecutively.
        if n == 0:
            return len(tasks)

        # count frequency of tasks
        counts = Counter(tasks)

        # init our max heap
        max_heap = [-freq for freq in counts.values()]
        heapq.heapify(max_heap)
    
        # init our cooldown queue for when a task has been executed
        cooldown_queue = deque()

        # init our time variable
        time = 0

        while max_heap or cooldown_queue:
            # every loop increment time for ans
            time += 1

            # check if the task at the front of the queue has finished 
            if cooldown_queue and cooldown_queue[0][1] == time:
                # get the count and push to the heap for execution 
                ready_cnt, _ = cooldown_queue.popleft()
                heapq.heappush(max_heap, ready_cnt)

            if max_heap:
                # execute the highest priority task and increment the count as neg frequencies
                cnt = heapq.heappop(max_heap)
                cnt += 1

                # if still tasks of this type to execute append this to the cooldown queue
                if cnt < 0:
                    cooldown_queue.append([cnt, time + n +1])

        return time

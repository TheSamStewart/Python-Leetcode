'''
solve using min heap

init the min heap with all current values

if the size of the heap exceeds k, we remove the item at the top of the min heap - 
this ensures the kth largest is stored at the root of the heap
'''

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.k = k
        self.nums = nums

        heapq.heapify(self.nums)

        while len(nums) > k:

            heapq.heappop(self.nums)
        

    def add(self, val: int) -> int:

        #push the new value

        heapq.heappush(self.nums,val)

        #if the size of the min heap exceeds K, pop the smallest value

        while len(self.nums) > self.k:

            heapq.heappop(self.nums)

        return self.nums[0]
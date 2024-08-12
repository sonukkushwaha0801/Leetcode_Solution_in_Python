# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)  # Convert the list into a heap
        # Keep only the k largest elements in the heap
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)
        return self.min_heap[0]
    
# Another way:
class KthLargest:

    def __init__(self, k: int, nums:list[int]) -> None:
        nums.append(float('-inf'))
        self.heap = sorted(nums)[-k:]

    def add(self, val: int) -> int:
        heapq.heappushpop(self.heap, val)
        return self.heap[0]


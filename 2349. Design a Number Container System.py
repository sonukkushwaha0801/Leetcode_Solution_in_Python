# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

class NumberContainers:

    def __init__(self):
        self.index_num = {} # index: num at index
        self.num_indices = {} # num: min heap of indices where num has been

    def change(self, index: int, number: int) -> None:
        self.index_num[index] = number # set number for index
        
        if number not in self.num_indices: 
            self.num_indices[number] = [] # make heap if new num
        heapq.heappush(self.num_indices[number], index) # add index to min heap

    def find(self, number: int) -> int:
        if number not in self.num_indices: 
            return -1 # no index with number
            
        pos_indices = self.num_indices[number]
        while pos_indices:
            min_index = pos_indices[0] # check lowest index
            
            if self.index_num[min_index] == number: 
                return min_index # valid index, found num at index

            heapq.heappop(pos_indices) # invalid index, new num at index
        
        return -1 # no valid index found
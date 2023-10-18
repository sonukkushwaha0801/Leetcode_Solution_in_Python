# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from random import random
class RandomizedSet:
    def __init__(self):
        self.data_map = {} 
        self.data = [] 

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False
        self.data_map[val] = len(self.data)
        self.data.append(val)
        
        return True

    def remove(self, val: int) -> bool:
        if not val in self.data_map:
            return False

        last_elem_in_list = self.data[-1]
        index_of_elem_to_remove = self.data_map[val]

        self.data_map[last_elem_in_list] = index_of_elem_to_remove
        self.data[index_of_elem_to_remove] = last_elem_in_list

        self.data[-1] = val

        self.data.pop()

        self.data_map.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)

#Another Way:
class RandomizedSet:

    def __init__(self):
        self.num_map = {}
        self.num_list = []
        

    def insert(self, val: int) -> bool:

        res = val not in self.num_map
        if res:
            self.num_map[val] = len(self.num_list)
            self.num_list.append(val)

        return res
        

    def remove(self, val: int) -> bool:

        res = val in self.num_map
        if res:
            index = self.num_map[val] 
            last_val = self.num_list[-1]

            self.num_list[index] = last_val
            self.num_list.pop()

            self.num_map[last_val] = index
            del self.num_map[val]


        return res 
        

    def getRandom(self) -> int:

        return random.choice(self.num_list)
        
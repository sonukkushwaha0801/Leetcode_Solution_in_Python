# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.capcaity = capacity 
        self.cache = deque()
        self.dicty = {}
        

    def get(self, key: int) -> int:
        if key not in self.dicty:
            return -1
        self.cache.remove(key)
        self.cache.appendleft(key)
        value = self.dicty[key]
        return value
        

    def put(self, key: int, value: int) -> None:
        if key not in self.dicty:
            if len(self.cache ) == self.capcaity:
                oldest = self.cache.pop()
                del self.dicty[oldest]

                self.dicty[key] = value
                self.cache.appendleft(key)
            else:
                

                self.dicty[key] = value
                self.cache.appendleft(key)

        else: 
            self.cache.remove(key)   

            self.dicty[key] = value
            self.cache.appendleft(key)
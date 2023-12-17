# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import defaultdict
import heapq
from sortedcontainers import Sortedlist, Sortedlist

class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.mp = {}
        self.data = defaultdict(Sortedlist)
        for food, cuisine, rating in zip(foods, cuisines, ratings): 
            self.mp[food] = (cuisine, rating)
            self.data[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.mp[food]
        self.mp[food] = cuisine, newRating
        self.data[cuisine].remove((-rating, food))
        self.data[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.data[cuisine][0][1]
    
# Another way:
class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.rating = {}
        self.cuisines = defaultdict(list)
        self.food_cuisine = {}
        
        for i in range(len(foods)):
            food, r, cuisine = foods[i], ratings[i], cuisines[i]
            self.rating[food] = -r
            self.food_cuisine[food] = cuisine
            heapq.heappush(self.cuisines[cuisine], (-r, food))
        

    def changeRating(self, food: str, newRating: int) -> None:
        self.rating[food] = -newRating
        cuisine = self.food_cuisine[food]
        heapq.heappush(self.cuisines[cuisine], (-newRating, food))
        

    def highestRated(self, cuisine: str) -> str:
        while self.rating[self.cuisines[cuisine][0][1]] != self.cuisines[cuisine][0][0]:
            heapq.heappop(self.cuisines[cuisine])
            
        return self.cuisines[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
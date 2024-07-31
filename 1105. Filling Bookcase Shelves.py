# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from typing import List

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        return self.arrangeBooks(books, shelfWidth)

    def arrangeBooks(self, books: List[List[int]], maxShelfWidth: int) -> int:
        minHeights = [float('inf')] * (len(books) + 1)
        minHeights[0] = 0

        for bookIndex in range(1, len(books) + 1):
            currentShelfHeight = 0
            currentShelfWidth = 0

            for lastBook in range(bookIndex - 1, -1, -1):
                currentBookThickness, currentBookHeight = books[lastBook]

                if currentShelfWidth + currentBookThickness > maxShelfWidth:
                    break

                currentShelfWidth += currentBookThickness
                currentShelfHeight = max(currentShelfHeight, currentBookHeight)

                currentArrangementHeight = minHeights[lastBook] + currentShelfHeight
                minHeights[bookIndex] = min(minHeights[bookIndex], currentArrangementHeight)

        return minHeights[len(books)]
    
# Another way:
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        cache={}
        def helper(i):
            if i==len(books):
                return 0
            if i in cache:
                return cache[i]
            curr_width=shelfWidth
            max_height=0
            cache[i]=float("inf")
            for j in range(i,len(books)):
                width,height=books[j]
                if curr_width<width:
                    break
                curr_width-=width
                max_height=max(max_height,height)
                cache[i]=min(
                    cache[i],
                    helper(j+1)+max_height
                )
            return cache[i]
        return helper(0)

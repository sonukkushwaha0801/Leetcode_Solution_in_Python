# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList):
        self.nestedList = nestedList
        self.flattenedList = []
        self.currentIndex = 0
        def flatten(currentList):
            for item in currentList:
                if item.isInteger():
                    self.flattenedList.append(item.getInteger())
                else:
                    flatten(item.getList())
        
        flatten(self.nestedList)

    def next(self):
        number = self.flattenedList[self.currentIndex]
        self.currentIndex += 1
        return number
    def hasNext(self):
        return self.currentIndex < len(self.flattenedList)
    
# Another Way:
class NestedIterator:
    def __init__(self, nestedList):
        self.stack = nestedList[::-1]

    def next(self):
        return self.stack.pop().getInteger()

    def hasNext(self):
        while self.stack:
            if self.stack[-1].isInteger():
                return True
            self.stack.extend(self.stack.pop().getList()[::-1])
        return False
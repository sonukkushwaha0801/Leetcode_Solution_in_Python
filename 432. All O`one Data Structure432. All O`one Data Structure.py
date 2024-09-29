# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# Solution:
class AllOne:

    def __init__(self):
        self.h = {}
        

    def inc(self, key: str) -> None:
        if key in self.h:
            self.h[key] += 1
        else:
            self.h[key] = 1

    def dec(self, key: str) -> None:
        if key in self.h:
            if self.h[key] > 1:
                self.h[key] -= 1
            else:
                del self.h[key]

    def getMaxKey(self) -> str:
        if not self.h:
            return ""
        return max(self.h, key=self.h.get)

    def getMinKey(self) -> str:
        if not self.h:
            return ""
        return min(self.h, key=self.h.get)
    
# Another way:


class AllOne:
    def __init__(self):
        self.minCount = 0
        self.maxCount = 0
        self.bucket = LinkedList()
        self.mapper = {} 

    def inc(self, key: str) -> None:
        node = self.bucket.head if key not in self.mapper else self.mapper[key]
        new_node = self.bucket.incrementElement(node, key)
        self.mapper[key] = new_node

    def dec(self, key: str) -> None:
        node = self.mapper[key]
        new_node = self.bucket.decrementElement(node, key)
        if new_node.count == 0:
            new_node.removeElement(key)
            del self.mapper[key]
        else:
            self.mapper[key] = new_node

    def getMaxKey(self) -> str:
        max_node = self.bucket.tail.prev
        if max_node.count == 0:
            return ""
        for e in max_node.keys:
            return e

    def getMinKey(self) -> str:
        min_node = self.bucket.head.next
        if min_node.count < float("inf"):
            for e in min_node.keys:
                return e
        else:
            return ""
    

class LinkedList:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(float("inf"))
        self.head.next = self.tail
        self.tail.prev = self.head

    def decrementElement(self, node, key):
        node.removeElement(key)
        prevNode = node.prev
        newCount = node.count-1
        correctNode = None
        if prevNode.count == newCount:
            correctNode = prevNode
        else:
            # insert new node
            correctNode = self.insertNext(prevNode, newCount)
        
        if not node.keys:
            self.pop(node)

        correctNode.addElement(key)
        return correctNode

    def incrementElement(self, node, key):
        if node.count != 0:
            node.removeElement(key)
        newCount = node.count + 1
        correctNode = None
        if node.next.count == newCount:
            correctNode = node.next
        else:
            correctNode = self.insertNext(node, newCount)

        correctNode.addElement(key)
        if not node.keys:
            self.pop(node)
        
        return correctNode


    def insertNext(self, node, count):
        nextNode = node.next

        new_node = Node(count)
        new_node.prev = node
        new_node.next = nextNode

        node.next = new_node
        nextNode.prev = new_node

        return new_node

    def pop(self, node):
        if node.count == 0 or node.count == float("inf"):
            return

        prev = node.prev
        nextNode = node.next

        prev.next = nextNode
        nextNode.prev = prev
        return



class Node:
    def __init__(self, count):
        self.keys = set()
        self.count = count
        self.prev = None
        self.next = None

    def removeElement(self, key):
        self.keys.remove(key)

    def addElement(self, key):
        self.keys.add(key)

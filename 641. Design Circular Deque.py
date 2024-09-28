# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# Solution:

class Node:
    def __init__(self, value):
        self.val = value
        self.prev = None
        self.next = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.count = 0
        self.n = k
        self.front = None
        self.rear = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = Node(value)
        if self.front is None and self.rear is None:
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = Node(value)
        if self.front is None and self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            if self.front:
                self.front.prev = None
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            if self.rear:
                self.rear.next = None
        self.count -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.rear.val

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.n

# Another way:

class MyCircularDeque:

    def __init__(self, k: int):
        self.q = [0 for _ in range(k + 1)]
        self.f = 0
        self.b = 0
        self.len = k + 1

    def insertFront(self, value: int) -> bool:
        if (self.b + 1) % self.len == (self.f) % self.len: return False
        self.f = (self.f - 1) % self.len
        self.q[self.f] = value
        return True

    def insertLast(self, value: int) -> bool:
        if (self.b + 1) % self.len == (self.f) % self.len: return False
        self.q[self.b] = value
        self.b = (self.b + 1) % self.len
        return True


    def deleteFront(self) -> bool:
        if self.b == self.f: return False
        self.f = (self.f + 1) % self.len
        return True
        

    def deleteLast(self) -> bool:
        if self.b == self.f: return False
        self.b = (self.b - 1) % self.len
        return True
        

    def getFront(self) -> int:
        if self.b == self.f: return -1
        return self.q[self.f]

    def getRear(self) -> int:
        if self.b == self.f: return -1
        return self.q[(self.b - 1) % self.len]
        

    def isEmpty(self) -> bool:
        return self.b == self.f
        

    def isFull(self) -> bool:
        return (self.b + 1) % self.len == self.f
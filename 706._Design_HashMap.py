# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class MyHashMap:
    def __init__(self):
        self.size = 10
        self.mp = [[] for _ in range(self.size)]

    def hash(self, key):
        return key % self.size

    def put(self, key, value):
        i = self.hash(key)
        bucket = self.mp[i]

        for idx, pair in enumerate(bucket):
            if pair[0] == key:
                bucket[idx] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key):
        i = self.hash(key)
        bucket = self.mp[i]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]

        return -1

    def remove(self, key):
        i = self.hash(key)
        bucket = self.mp[i]

        for idx, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[idx]
                return

# Another Way:
class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [None] * self.size
    def put(self, key: int, value: int) -> None:
        index = key % self.size
        if self.buckets[index] is None:
            self.buckets[index] = []
        for i, (existing_key, existing_value) in enumerate(self.buckets[index]):
            if existing_key == key:
                self.buckets[index][i] = (key, value)
                return
        self.buckets[index].append((key, value))
    def get(self, key: int) -> int:
        index = key % self.size
        if self.buckets[index] is None:
            return -1
        for existing_key, existing_value in self.buckets[index]:
            if existing_key == key:
                return existing_value
        return -1
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.buckets[index] is None:
            return
        for i, (existing_key, existing_value) in enumerate(self.buckets[index]):
            if existing_key == key:
                del self.buckets[index][i]
                return
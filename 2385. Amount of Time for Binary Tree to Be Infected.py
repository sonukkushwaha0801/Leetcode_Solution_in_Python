# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:

from collections import deque, defaultdict

class Solution:
    def amountOfTime(self, root, start):
        map = defaultdict(set)
        self.convert(root, 0, map)
        q = deque()
        q.append(start)
        minute = 0
        visited = set()
        visited.add(start)

        while q:
            level_size = len(q)
            while level_size > 0:
                current = q.popleft()

                for num in map[current]:
                    if num not in visited:
                        visited.add(num)
                        q.append(num)
                level_size -= 1
            minute += 1
        return minute - 1

    def convert(self, current, parent, map):
        if not current:
            return
        if current.val not in map:
            map[current.val] = set()
        adjacent_list = map[current.val]
        if parent != 0:
            adjacent_list.add(parent)
        if current.left:
            adjacent_list.add(current.left.val)
        if current.right:
            adjacent_list.add(current.right.val)
        self.convert(current.left, current.val, map)
        self.convert(current.right, current.val, map)

# Another way:

class Solution:
    def amountOfTime(self, root, start: int) -> int:
        self.start_node = None
        
        def mark_parent(node, _parent):
            if not node:
                return 

            if node.val == start:
                self.start_node = node

            node.parent = _parent 
            mark_parent(node.left, node)
            mark_parent(node.right, node)

        mark_parent(root, None) 

        count = 0
        queue = deque()
        _set = set()
        queue.append((self.start_node, -1))

        while queue:
            curr, time = queue.popleft() 
            if curr not in _set:
                _set.add(curr)
                count = max(count, time+1)
                if curr.left is not None and curr.left not in _set:
                    queue.append((curr.left, time+1))
                if curr.right is not None and curr.right not in _set:
                    queue.append((curr.right, time+1))
                if curr.parent is not None and curr.parent not in _set:
                    queue.append((curr.parent, time+1))
            
                
        return count

    

        
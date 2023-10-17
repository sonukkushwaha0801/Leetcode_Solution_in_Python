# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from queue import Queue
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]) -> bool:
        all_child = [ val for val in leftChild+rightChild if val!=-1]
        roots = list(set(range(n))-set(all_child))
        if len(all_child)+1 != n or len(roots)!=1: return False
        root,cnt = roots[0] , 0
        q = Queue()
        q.put(root)
        while not q.empty():
            val = q.get()
            cnt+=1
            if leftChild[val]!=-1: q.put(leftChild[val])
            if rightChild[val]!=-1: q.put(rightChild[val])

        return cnt==n

# Another way:
from collections import defaultdict

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]) -> bool:
        graph = defaultdict(list)
        indeg = [0] * n

        # Build the graph and calculate in-degrees
        for i in range(n):
            left, right = leftChild[i], rightChild[i]
            if left != -1:
                graph[i].append(left)
                indeg[left] += 1
                if indeg[left] > 1:
                    return False
            if right != -1:
                graph[i].append(right)
                indeg[right] += 1
                if indeg[right] > 1:
                    return False

        # Find the root node (in-degree 0)
        root = -1
        for i in range(n):
            if indeg[i] == 0:
                if root != -1:
                    return False  # Multiple roots found
                root = i

        if root == -1:
            return False  # No root found

        visited = set()
        stack = [root]

        while stack:
            node = stack.pop()
            if node in visited:
                return False
            visited.add(node)

            for child in graph[node]:
                indeg[child] -= 1
                if indeg[child] == 0:
                    stack.append(child)

        return len(visited) == n

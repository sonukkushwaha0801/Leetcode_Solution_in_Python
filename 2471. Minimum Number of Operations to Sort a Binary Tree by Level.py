# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

class Solution:
    def minimumSwaps(self, arr):
        n, swaps = len(arr), 0
        store = [(arr[i], i) for i in range(n)]
        store.sort()
        
        visited = [0] * n
        for i in range(n):
            if visited[i] or i == store[i][1]: continue

            x, cycle_count = i, 0
            while not visited[x]:
                visited[x] = 1
                x = store[x][1]
                cycle_count += 1
            swaps += cycle_count - 1

        return swaps

    def minimumOperations(self, root) -> int:
        minSwaps = 0
        queue = deque([root])
        while(queue):
            arr = []
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                arr.append(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            minSwaps += self.minimumSwaps(arr)

        return minSwaps
    
# Another way:
from collections import deque
class Solution:
    def minimumOperations(self, root) -> int:

        q=deque()
        q.append(root)
        count=0
        while q:
            n=len(q)
            arr_level=[]
            for _ in range(n):
                curr=q.popleft()
                arr_level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
 
            sort_t = sorted(arr_level)
            maps = {v: i for i, v in enumerate(sort_t)}
            vis = set()

            for i in range(len(arr_level)):
                while arr_level[i]!=sort_t[i]:
                    count+=1
                    id=maps[arr_level[i]]
                    temp=arr_level[i]
                    arr_level[i]=arr_level[id]
                    arr_level[id]=temp

        return count
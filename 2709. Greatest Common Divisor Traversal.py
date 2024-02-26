# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from collections import defaultdict, deque


primes = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
    179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
    283, 293, 307, 311, 313
]

class Solution:
    def canTraverseAllPairs(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        nums = set(nums)
        if 1 in nums:
            return False
        if len(nums) == 1:
            return True

        factor_graph = defaultdict(set)
        for x in nums:          
            if x in factor_graph:
                continue
            factors = []
            for p in primes:
                if p > x:
                    break
                if x % p != 0:
                    continue
                factors.append(p)
                while x % p == 0:
                    x //= p
            
            if x > 1:
                factors.append(x)

            for i in range(len(factors)):
                for j in range(i, len(factors)):
                    factor_graph[factors[i]].add(factors[j])
                    factor_graph[factors[j]].add(factors[i])
        
        
        visited = {k: False for k in factor_graph.keys()}
        start = list(factor_graph.keys())[0]
        visited[start] = True
        q = deque([start])
        while q:
            p = q.popleft()
            for n in factor_graph[p]:
                if visited[n]:
                    continue
                visited[n] = True
                q.append(n)
        
        return all(visited.values())
    
# Another way:
class UnionFind:
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.rank = [1]*n

    def find(self,x):
        while x!=self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self,n1,n2):
        p1,p2 = self.find(n1),self.find(n2)

        if p1==p2:
            return 0

        if self.rank[p1]<self.rank[p2]:
            self.par[p1]=p2
            self.rank[p2]+=1
        else:
            self.par[p2]=p1
            self.rank[p1]+=1
        
        return 1

class Solution:
    def canTraverseAllPairs(self, nums: list[int]) -> bool:
        length = len(nums)
        uf = UnionFind(length)
        factorIndex = {}
        ans = length

        for i,n in enumerate(nums):
            f=2
            while f*f<=n:
                if n%f==0:
                    if f in factorIndex:
                        ans-=uf.union(factorIndex[f],i)
                    else:
                        factorIndex[f] = i
                    while n%f==0:
                        n=n//f
                f+=1

            if n>1:
                if n in factorIndex:
                    ans-=uf.union(factorIndex[n],i)
                else:
                    factorIndex[n] = i

        return ans==1

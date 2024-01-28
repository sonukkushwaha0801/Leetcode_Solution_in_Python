# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
import heapq
class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int):
        heap=[]
        heapq.heappush(heap,(nums1[0]+nums2[0],0,0))
        visited=set()
        visited.add((0,0))
        output=[]
        while len(output)<k and heap:
            val=heapq.heappop(heap)
            output.append([nums1[val[1]],nums2[val[2]]])
            if(val[1]+1<len(nums1) and (val[1]+1,val[2]) not in visited):
                heapq.heappush(heap,(nums1[val[1]+1]+nums2[val[2]],val[1]+1,val[2]))
                visited.add((val[1]+1,val[2]))
            if(val[2]+1<len(nums2) and (val[1],val[2]+1) not in visited):
                heapq.heappush(heap,(nums1[val[1]]+nums2[val[2]+1],val[1],val[2]+1))
                visited.add((val[1],val[2]+1))
        return output
from heapq import heappush, heappop
# Another way:
class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        ans = []
        n1, n2 = len(nums1), len(nums2)
        visited = set()
        hp = []
        hp.append((nums1[0]+nums2[0],(0,0)))
        visited.add((0,0))
        count = 0
        while k and hp:
            val, (i,j) = heappop(hp)
            ans.append([nums1[i],nums2[j]])

            if i+1<n1 and (i+1,j) not in visited:
                heappush(hp, (nums1[i+1]+nums2[j],(i+1,j)))
                visited.add((i+1,j))

            if j+1<n2 and (i, j+1) not in visited:
                heappush(hp,(nums1[i]+nums2[j+1], (i,j+1)))
                visited.add((i,j+1))

            k -= 1

        return ans
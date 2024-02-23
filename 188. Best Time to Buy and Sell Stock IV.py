# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from heapq import heappop, heappush


class DoubleLinklistNode:
    def __init__(self, ind, pre = None, next = None):
        self.ind = ind
        self.pre = pre if pre else self
        self.next = next if next else self

class Solution:
    def MinMaxlist(self, arr: list[int]) -> list[int]:
        n = len(arr)
        if n == 0:
            return []
        sign = -1
        res = [9999]
        for num in arr:
            if num * sign > res[-1] * sign:
                res[-1] = num
            else:
                res.append(num)
                sign *= -1
        if len(res) & 1:
            res.pop()
        return res
    def maxProfit(self, k: int, prices: list[int]) -> int:
        newP = self.MinMaxlist(prices)
        n = len(newP)
        m = n // 2
        res = 0
        for i in range(m):
            res += newP[i*2+1] - newP[i*2]
        if m <= k:
            return res
        head, tail = DoubleLinklistNode(-1), DoubleLinklistNode(-1)
        Nodelist = [DoubleLinklistNode(0, head)]
        for i in range(1, n):
            Nodelist.append(DoubleLinklistNode(i, Nodelist[-1]))
            Nodelist[i-1].next = Nodelist[i]
        Nodelist[n-1].next = tail
        head.next, tail.pre = Nodelist[0], Nodelist[n-1]
        heap = []
        for i in range(n-1):
            if i&1:
                heappush(heap, [newP[i] - newP[i+1], i, i+1, 0])
            else:
                heappush(heap, [newP[i+1] - newP[i], i, i+1, 1])
        while m > k:
            loss, i, j, t = heappop(heap)
            if Nodelist[i] == None or Nodelist[j] == None: continue
            m -= 1
            res -= loss
            nodei, nodej = Nodelist[i], Nodelist[j]
            nodel, noder = nodei.pre, nodej.next
            l, r = nodel.ind, noder.ind
            valL, valR = newP[l], newP[r]
            noder.pre, nodel.next = nodel, noder
            Nodelist[i], Nodelist[j] = None, None
            if t == 0:
                heappush(heap, [valR - valL, l, r, 1])
            elif l != -1 and r != -1:
                heappush(heap, [valL - valR, l, r, 0])
        return res
    
# Another way:
class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        def func(i,buy,prices,ct,dic):
            if i>=len(prices) or ct==0:
                return 0
            if (i,buy,ct) in dic:
                return dic[(i,buy,ct)]
            x,y,a,b=0,0,0,0
            if buy:
                x=-prices[i]+func(i+1,False,prices,ct,dic)
                y=0+func(i+1,buy,prices,ct,dic)
            else:
                a=prices[i]+func(i+1,True,prices,ct-1,dic)
                b=0+func(i+1,buy,prices,ct,dic)
            dic[(i,buy,ct)]=max(a,b,x,y)
            return max(a,b,x,y)
        return func(0,True,prices,k,{})
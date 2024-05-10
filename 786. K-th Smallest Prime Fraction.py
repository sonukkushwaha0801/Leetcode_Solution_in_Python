# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        minHeap = []
        N = len(arr)
        for i in range(N):
            for j in range(i + 1, N):
                heappush(minHeap, (arr[i] / arr[j], (arr[i], arr[j])))
        for _ in range(k):
            a, b = heappop(minHeap)[1]
        return [a, b]
    
# ANother way:
class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        n = len(arr)
        
        # Returns number of fractions smaller than or equal to x
        
        def func(x):
            i,j = 0,1 
            count = a = b = 0
            
            while max(i,j) < n:
                if arr[i]/arr[j] <= x:
                    count += (n-j)
                    
                    if a*arr[j] <= b*arr[i]:
                        a,b = arr[i],arr[j]
                        
                    i += 1 
                else:
                    j += 1 
                    
            return [count,a,b]
        
        low, high = 0, 1 
        
        while low < high:
            mid = (low+high)/2 
            ans = func(mid)
            
            if ans[0] < k:
                low = mid 
            elif ans[0] > k:
                high = mid 
            else:
                return ans[1:]
            
        return []
                
        
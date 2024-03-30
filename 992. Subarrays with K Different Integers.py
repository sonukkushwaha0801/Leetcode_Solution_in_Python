# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        cnt=[0]*(len(nums)+1)
        ans=0
        l=0
        m=0
        for num in nums:
            cnt[num]+=1
            if cnt[num]==1:
                k-=1
                if k<0:
                    cnt[nums[m]]=0
                    m+=1
                    l=m
            if k<=0:
                while cnt[nums[m]]>1:
                    cnt[nums[m]]-=1
                    m+=1
                ans+=m-l+1
        return ans                        
    
# Another way:
class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:

        def subarraysWithAtMost(kEle):
            freq = defaultdict(int)
            l = ans = 0

            for r,num in enumerate(nums):
                freq[num]+=1
                while len(freq)>kEle:
                    freq[nums[l]]-=1
                    if freq[nums[l]]==0:
                        del freq[nums[l]]
                    l+=1
                
                ans+=r-l+1
            
            return ans

        return subarraysWithAtMost(k)-subarraysWithAtMost(k-1)
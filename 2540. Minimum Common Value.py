# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        i = 0
        j = 0
        common = float('inf')

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                common = nums1[i]
                break
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return common if common != float('inf') else -1
    
# Another way:
class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        n1, n2= len(nums1), len(nums2)
        p1, p2=0, 0
        while p1<n1 and p2<n2:
            x=nums1[p1]
            y=nums2[p2]
            if x==y: return x
            elif x>y: p2+=1
            else: p1+=1
        return -1
        
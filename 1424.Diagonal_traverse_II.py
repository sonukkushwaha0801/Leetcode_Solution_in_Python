# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        mp,ans={},[]
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i+j not in mp:mp[i+j]=[nums[i][j]]
                else:mp[i+j].append(nums[i][j])
        for i in mp:ans.extend(mp[i][::-1])
        return ans

# Another way:
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        arr = []
        for i in range(len(nums)-1,-1,-1):
            for j in range(len(nums[i])-1,-1,-1):
                arr.append([i+j,nums[i][j]])
        arr.sort(key=lambda x:x[0])
        for _,j in arr:
            res.append(j)          
        return res
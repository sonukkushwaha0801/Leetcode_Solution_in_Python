#Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = ""

        index = 0
        for bin_num in nums:
            ans = ans + str(1 - int(bin_num[index]))
            index+=1
        return ans
    
# Another way:
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums[0])
        ans=['0']*n
        for i, x in enumerate(nums):
            if x[i]=='0':
                ans[i]='1'
            else:
                ans[i]='0'
        return "".join(ans)
                
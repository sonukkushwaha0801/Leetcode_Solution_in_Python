# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        prefix_sum = [0] * n
        suffix_sum = [0] * n

        prefix_sum[0] = nums[0]
        suffix_sum[n - 1] = nums[n - 1]

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
            suffix_sum[n - i - 1] = suffix_sum[n - i] + nums[n - i - 1]

        for i in range(n):
            current_absolute_diff = ((nums[i] * i) - prefix_sum[i]) + (suffix_sum[i] - (nums[i] * (n - i - 1)))
            result[i] = current_absolute_diff

        return result
    
# Another way:
class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        sm,pr=sum(nums),0
        for i in range(len(nums)):
            pr+=nums[i]
            nums[i]=(((i+1)*nums[i]-pr)+(sm-pr)-(len(nums)-i-1)*nums[i])
        return nums

# Addition one:
class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        pr=[None]*len(nums)
        pr[0]=nums[0]
        for i in range(1,len(nums)):pr[i]=pr[i-1]+nums[i]
        su=[None]*len(nums)
        su[len(nums)-1]=nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):su[i]=su[i+1]+nums[i]
        return [(nums[i]*(i+1)-pr[i])+su[i]-nums[i]*(len(nums)-i) for i in range(len(nums))]
# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
        temp = sorted(list(set(nums)))
        i = 0
        j = 1
        count = 1
        curr = 1
        while j < len(temp):
            if temp[j] - 1 == temp[i]:

                curr += 1
                count = max(curr, count)
            else:
                curr = 1
            
            i = j
            j += 1
        return count

# Another way:
class Solution:
    def longestConsecutive(self, arr: list[int]) -> int:
        nums, ans = set(arr), 0
        while len(nums)>0:
            nextt = next(v for v in nums)
            prev = nextt-1
            while nextt in nums:
                nums.discard(nextt)
                nextt += 1
            while prev in nums:
                nums.discard(prev)
                prev -= 1
            ans = max(ans, nextt-prev-1)

        return ans
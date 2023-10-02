# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ranges = []
        start, end = nums[0], nums[0]

        for num in nums[1:]:
            if num == end + 1:
                end = num
            else:
                ranges.append(f"{start}->{end}" if start != end else str(start))
                start, end = num, num

        ranges.append(f"{start}->{end}" if start != end else str(start))

        return ranges
# Another Type:
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = [] # [start, end] or [x, y]
        for i, n in enumerate(nums):
            if ranges and ranges[-1][1] == n-1:
                ranges[-1][1] = n
            else:
                ranges.append([n, n])

        return [f'{x}->{y}' if x != y else f'{x}' for x, y in ranges]
# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type 1:
class Solution:
    def find132pattern(self,nums):
        n = len(nums)
        if n < 3:
            return False

        stack = []
        third = float('-inf')

        for i in range(n - 1, -1, -1):
            if nums[i] < third:
                return True
            while stack and nums[i] > stack[-1]:
                third = stack.pop()
            stack.append(nums[i])

        return False

# Type 2:
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        length = len(nums)
        if length < 3:
            return False
        decreasing_stack = deque()
        max_third_element = float('-inf')
        for i in range(length - 1, -1, -1):
            current_number = nums[i]
            if current_number < max_third_element:
                return True
            while decreasing_stack and decreasing_stack[0] < current_number:
                max_third_element = decreasing_stack.popleft()
            decreasing_stack.appendleft(current_number)

        return False 
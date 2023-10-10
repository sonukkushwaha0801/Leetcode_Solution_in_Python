# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def minOperations(self, nums):
        unq_element = set()
        new_list = []
        for num in nums:
            if num not in unq_element:
                new_list.append(num)
                unq_element.add(num)
        new_list.sort()
        last_ind = 0
        size = len(new_list)
        operation = float('inf')
        for ind in range(size):
            while last_ind < size and new_list[last_ind] - new_list[ind] < len(nums):
                last_ind += 1
            opReq = len(nums) - (last_ind - ind)
            operation = min(operation, opReq)
        return operation

# Another Way:
class Solution:
    def minOperations(self, nums):
        maxi = 0  
        count = 0  
        n = len(nums) - 1 
        l = 0  
        nums.sort()  
        i = 0
        while i < len(nums):
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
                continue
            nums[l] = nums[i]
            l += 1
            i += 1
        i = 0
        j = 0
        while i < l:
            while j < l and (nums[j] - nums[i]) <= n:
                count += 1
                j += 1
            maxi = max(maxi, count)
            count -= 1
            i += 1
        return len(nums) - maxi
    

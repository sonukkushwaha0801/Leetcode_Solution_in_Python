# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return 

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next       

        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

# Another way:
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        array = []
        while temp:
            array.append(temp.val)
            temp = temp.next
        ans = []
        l, r = 0, len(array)-1
        while l <= r:
            if l != r:
                ans.append(array[l])
                ans.append(array[r])
                l += 1
                r -= 1
            else:
                ans.append(array[l])
                l += 1
                r -= 1
        temp = head
        i = 0
        while temp and i < len(ans):
            temp.val = ans[i]
            temp = temp.next
            i += 1
        return head
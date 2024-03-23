# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_vals = []
        while head:
            list_vals.append(head.val)
            head = head.next
        
        left, right = 0, len(list_vals) - 1
        while left < right and list_vals[left] == list_vals[right]:
            left += 1
            right -= 1
        return left >= right
    
# Another way:
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = self.reverseList(slow.next)

        slow = slow.next

        while slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        return True

    def reverseList(self, head: ListNode) -> ListNode:
        pre = None

        while head:
            next_node = head.next
            head.next = pre
            pre = head
            head = next_node
        return pre
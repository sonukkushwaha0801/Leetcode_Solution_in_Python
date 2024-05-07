# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
# Definition for singly-linked list.

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, node = None, head

        while node:
            next_temp = node.next
            node.next = prev
            prev, node = node, next_temp
        head = prev

        node = head
        carry = 0
        while node:
            current_double = node.val * 2 + carry
            node.val = current_double % 10
            carry = current_double // 10
            prev = node
            node = node.next

        if carry > 0:
            prev.next = ListNode(carry)

        prev, node = None, head
        while node:
            next_temp = node.next
            node.next = prev
            prev, node = node, next_temp

        return prev
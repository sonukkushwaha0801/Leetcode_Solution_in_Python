# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        prefix_sums = {0: dummy}
        current = head

        while current:
            prefix_sum += current.val
            if prefix_sum in prefix_sums:
                to_delete = prefix_sums[prefix_sum].next
                temp_sum = prefix_sum + to_delete.val
                while to_delete != current:
                    del prefix_sums[temp_sum]
                    to_delete = to_delete.next
                    temp_sum += to_delete.val
                prefix_sums[prefix_sum].next = current.next
            else:
                prefix_sums[prefix_sum] = current
            current = current.next

        return dummy.next
    
# Another way:
class Solution:
	def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:

		dummy = ListNode(0,head)
		pre = 0
		dic = {0: dummy}

		while head:
			pre+=head.val
			dic[pre] = head
			head = head.next

		head = dummy
		pre = 0
		while head:
			pre+=head.val
			head.next = dic[pre].next
			head = head.next

		return dummy.next
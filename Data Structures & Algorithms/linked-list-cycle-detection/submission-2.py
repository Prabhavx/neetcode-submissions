# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            head.val = 1.1
            if head.next:
                if head.next.val == 1.1: return True
            else:
                return False
            head = head.next
        return False
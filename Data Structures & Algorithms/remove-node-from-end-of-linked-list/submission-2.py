# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len = 0
        cur = head
        while cur:
            cur = cur.next
            len+=1

        indx = len-n
        if indx == 0: return head.next
        cur = head
        for i in range(len-1):
            if (i+1) == indx:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head
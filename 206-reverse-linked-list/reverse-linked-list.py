# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # Base case: return last node or None
        
        newhead = self.reverseList(head.next)
        head.next.next = head  # Reverse the link
        head.next = None       # Break the original link
        
        return newhead
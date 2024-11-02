"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dummy = cur = ListNode()
        stack = [head]
        while stack:
            node = stack.pop()
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
            cur.next = node
            node.prev = cur
            node.child = None
            cur = node
            dummy.next.prev = None
        return dummy.next

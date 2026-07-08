"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldCopy = {None:None}

        curr = head
        while curr:
            copy = Node(curr.val)
            oldCopy[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = oldCopy[curr]
            copy.random = oldCopy[curr.random]
            copy.next = oldCopy[curr.next]
            curr = curr.next
        
        return oldCopy[head]